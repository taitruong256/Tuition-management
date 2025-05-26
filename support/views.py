from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SupportRequestForm
from .models import SupportRequest

# Create your views here.

@login_required
def submit_request(request):
    # Lấy danh sách các yêu cầu đã gửi của sinh viên
    requests = SupportRequest.objects.filter(student=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            support = form.save(commit=False)
            support.student = request.user
            support.save()
            return render(request, 'support/submit_success.html')
    else:
        form = SupportRequestForm()
    return render(request, 'support/submit_request.html', {'form': form, 'requests': requests})
