from rest_framework import serializers,generics
from ..models import PayoutRequest

class PayoutRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutRequest
        fields = '__all__'

class PayoutRequestListCreateView(generics.ListCreateAPIView):
    queryset = PayoutRequest.objects.all()
    serializer_class = PayoutRequestSerializer

class PayoutRequestRetrieveView(generics.RetrieveAPIView):
    queryset = PayoutRequest.objects.all()
    serializer_class = PayoutRequestSerializer
    lookup_field = 'pk'