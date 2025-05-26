from django import forms
from .models import Invoice

class InvoiceRequestForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = []  # Có thể bổ sung trường nếu muốn sinh viên nhập thêm thông tin 