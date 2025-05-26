from django import forms
from .models import OtherFee

class OtherFeeForm(forms.ModelForm):
    class Meta:
        model = OtherFee
        fields = ['student', 'semester', 'name', 'amount', 'status']