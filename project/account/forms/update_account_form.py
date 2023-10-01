from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from account.models import Account

class UpdateAccountForm(forms.ModelForm):
    country_code = forms.CharField(max_length=5, required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Account  # Update this to your Account model
        fields = ('username', 'full_name', 'mobile_number', 'email', 'profile_image', 'activate_whatsapp')

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        country_code = self.cleaned_data.get('country_code')
        
        if country_code and not mobile_number.startswith(country_code):
            mobile_number = f'{country_code}{mobile_number}'
        
        if not mobile_number.startswith('+'):
            raise ValidationError(_('Mobile number must start with a plus sign (+).'))
        
        if not mobile_number[1:].isdigit() or len(mobile_number) < 10:
            raise ValidationError(_('Invalid mobile number format. It should contain at least 10 digits after the plus sign.'))
        
        return mobile_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError(_('Passwords do not match.'))

    def save(self, commit=True):
        account = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            account.set_password(password)
        
        if commit:
            account.save()
        
        return account
