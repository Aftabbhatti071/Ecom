

from django import forms

class PaymentForm(forms.Form):
    cardholder= forms.CharField()
    stripe_token = forms.CharField(widget=forms.HiddenInput)
