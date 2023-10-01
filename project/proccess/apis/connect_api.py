from rest_framework import serializers, generics
from ..models import Connect,ConnectRate

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = '__all__'

class ConnectRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectRate
        fields = '__all__'

class ConnectListCreateView(generics.ListCreateAPIView):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer

class ConnectRetrieveView(generics.RetrieveAPIView):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer
    lookup_field = 'pk'


class ConnectRateListCreateView(generics.ListCreateAPIView):
    queryset = ConnectRate.objects.all()
    serializer_class = ConnectRateSerializer

class ConnectRateRetrieveView(generics.RetrieveAPIView):
    queryset = ConnectRate.objects.all()
    serializer_class = ConnectRateSerializer
    lookup_field = 'pk'