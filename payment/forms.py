from django import forms
from .models import OnlinePayment

class OnlinePaymentForm(forms.ModelForm):
    class Meta:
        model = OnlinePayment
        fields = ['semester', 'amount', 'payment_method']
