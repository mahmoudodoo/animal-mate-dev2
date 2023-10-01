from django import forms
from account.models import Account  # Import your Account model here

class ConfirmEmailForm(forms.ModelForm):
    key = forms.CharField(max_length=255)

    class Meta:
        model = Account  # Update this to your Account model
        fields = ('key',)

class SendConfirmEmailForm(forms.Form):
    email = forms.CharField(max_length=255)
