from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from account.models import Account

class SignUpForm(UserCreationForm):
    accept = forms.BooleanField(required=True, help_text=_("Accept the terms and conditions."))

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'mobile_number', 'country')
        labels = {
            'country': _('Country'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = _("Username")
        self.fields['email'].widget.attrs['placeholder'] = _("Email")
        self.fields['password1'].widget.attrs['placeholder'] = _("Password")
        self.fields['password2'].widget.attrs['placeholder'] = _("Confirm Password")
        self.fields['full_name'].widget.attrs['placeholder'] = _("Full Name")
        self.fields['mobile_number'].widget.attrs['placeholder'] = _("Mobile Number")
        self.fields['country'].widget.attrs['placeholder'] = _("Country")
