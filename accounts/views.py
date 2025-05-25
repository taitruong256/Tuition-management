from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView
from django.urls import reverse_lazy
from .forms import StudentLoginForm, StudentPasswordResetForm, StudentPasswordChangeForm
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def home(request):
    return render(request, 'accounts/home.html')

# Create your views here.

class StudentLoginView(LoginView):
    form_class = StudentLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('login')

class StudentPasswordResetView(PasswordResetView):
    form_class = StudentPasswordResetForm
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        student_id = form.cleaned_data.get('student_id')
        email = form.cleaned_data.get('email')
        from .models import StudentUser
        if not StudentUser.objects.filter(student_id=student_id, email=email).exists():
            form.add_error('student_id', 'Mã số sinh viên hoặc email không đúng. Vui lòng nhập lại!')
            form.add_error('email', 'Mã số sinh viên hoặc email không đúng. Vui lòng nhập lại!')
            return self.form_invalid(form)
        return super().form_valid(form)

class StudentPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class StudentPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class StudentPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/profile.html', {'student': request.user})

class StudentPasswordChangeView(PasswordChangeView):
    form_class = StudentPasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = '/accounts/profile/'
