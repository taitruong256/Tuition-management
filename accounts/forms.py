from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from .models import StudentUser

class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Mã số sinh viên',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã số sinh viên'})
    )
    password = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu'})
    )

class StudentPasswordResetForm(PasswordResetForm):
    student_id = forms.CharField(
        label='Mã số sinh viên',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mã số sinh viên'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email của bạn'})
    )

class StudentPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Mật khẩu cũ',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu cũ'})
    )
    new_password1 = forms.CharField(
        label='Mật khẩu mới',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu mới'})
    )
    new_password2 = forms.CharField(
        label='Xác nhận mật khẩu mới',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu mới'})
    ) 