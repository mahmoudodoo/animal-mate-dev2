from django import forms
from ..models import Animal  # Import your Animal model here

class CreateNewAnimal(forms.ModelForm):
    class Meta:
        model = Animal  # Update this to your Animal model
        fields = '__all__'  # Use '__all__' to include all fields from the model in the form



class EditAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal  # Update this to your Animal model
        fields = '__all__'  # Use '__all__' to include all fields from the model in the form
