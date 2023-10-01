from rest_framework import serializers,generics
from ..models import Animal, AnimalPriceForStripe, AnimalRequest

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalPriceForStripeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalPriceForStripe
        fields = '__all__'

class AnimalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalRequest
        fields = '__all__'



class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalPriceForStripeListCreateView(generics.ListCreateAPIView):
    queryset = AnimalPriceForStripe.objects.all()
    serializer_class = AnimalPriceForStripeSerializer

class AnimalPriceForStripeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalPriceForStripe.objects.all()
    serializer_class = AnimalPriceForStripeSerializer


class AnimalRequestListCreateView(generics.ListCreateAPIView):
    queryset = AnimalRequest.objects.all()
    serializer_class = AnimalRequestSerializer

class AnimalRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalRequest.objects.all()
    serializer_class = AnimalRequestSerializer