# views.py
from rest_framework import generics,serializers
from ..models import Account
from django_countries.serializer_fields import CountryField


class CustomCountryField(serializers.Field):
    def to_representation(self, obj):
        # Convert the Country object to its code for JSON serialization
        return obj.code

    def to_internal_value(self, data):
        # Convert the code back to a Country object
        from django_countries.fields import Country
        return Country(data)

class AccountSerializer(serializers.ModelSerializer):
    country = CustomCountryField()
    class Meta:
        model = Account
        fields = '__all__'


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
