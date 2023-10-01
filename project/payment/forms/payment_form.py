from django import forms

class RequestPaymentForm(forms.Form):
    balance = forms.IntegerField()


class SendPaymentDataForm(forms.Form):
    routing_number = forms.CharField(max_length=255, required=False)
    account_number = forms.CharField(max_length=255)
