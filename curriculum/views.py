from django.shortcuts import render, get_object_or_404, redirect
from .models import CurriculumFramework
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden

# Create your views here.

# View chỉ xem, ai cũng xem được

def curriculum_framework_list(request):
    frameworks = CurriculumFramework.objects.all()
    return render(request, 'curriculum/curriculum_framework_list.html', {'frameworks': frameworks})

# Ví dụ view thêm (chỉ admin mới được phép)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_curriculum_framework(request):
    if request.method == 'POST':
        # Xử lý thêm mới
        pass
    return render(request, 'curriculum/add_curriculum_framework.html')

# Tương tự cho edit, delete: dùng @login_required và @user_passes_test(lambda u: u.is_superuser)
