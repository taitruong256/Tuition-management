from django.shortcuts import render, redirect
from .models import ClassSubject, Registration
from accounts.models import StudentUser
from curriculum.models import Subject, Semester
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from debt.models import TuitionDebt

@login_required
def register(request):
    # Lấy sinh viên đang đăng nhập
    student = request.user
    # Lấy curriculum của sinh viên
    curriculum = getattr(student, 'curriculum', None)
    semesters = Semester.objects.filter(curriculum=curriculum) if curriculum else Semester.objects.none()
    # Lấy học kỳ được chọn từ GET hoặc mặc định là học kỳ đầu tiên
    semester_id = request.GET.get('semester')
    if semesters:
        if semester_id:
            selected_semester = semesters.filter(id=semester_id).first()
        else:
            selected_semester = semesters.first()
    else:
        selected_semester = None
    # Lọc môn học và lớp học phần theo học kỳ
    subjects = Subject.objects.filter(semester=selected_semester) if selected_semester else Subject.objects.none()
    class_subjects = ClassSubject.objects.filter(subject__semester=selected_semester) if selected_semester else ClassSubject.objects.none()
    registered = Registration.objects.filter(student=student, class_subject__subject__semester=selected_semester) if selected_semester else Registration.objects.none()

    # Hủy đăng ký
    if request.method == 'POST' and 'cancel_registration' in request.POST:
        reg_id = request.POST.get('cancel_registration')
        reg = Registration.objects.filter(id=reg_id, student=student).first()
        if reg:
            reg.delete()
            messages.success(request, 'Hủy đăng ký thành công!')
        else:
            messages.error(request, 'Không tìm thấy đăng ký để hủy!')
        return redirect(f"{request.path}?semester={selected_semester.id if selected_semester else ''}")

    # Đăng ký mới
    if request.method == 'POST' and 'class_subject' in request.POST:
        class_subject_id = request.POST.get('class_subject')
        if class_subject_id:
            cs = ClassSubject.objects.get(id=class_subject_id)
            if not Registration.objects.filter(student=student, class_subject=cs).exists():
                reg = Registration.objects.create(student=student, class_subject=cs)
                subject = cs.subject
                TuitionDebt.objects.get_or_create(
                    student=student,
                    semester=subject.semester,
                    subject=subject,
                    defaults={
                        'theory_credits': subject.theory_credits,
                        'practice_credits': subject.practice_credits,
                        'status': 'unpaid',
                    }
                )
                messages.success(request, f'Đăng ký lớp học phần {cs} thành công!')
            else:
                messages.warning(request, 'Bạn đã đăng ký lớp học phần này rồi!')
        else:
            messages.error(request, 'Vui lòng chọn lớp học phần để đăng ký!')
        return redirect(f"{request.path}?semester={selected_semester.id if selected_semester else ''}")

    return render(request, 'registration/register.html', {
        'semesters': semesters,
        'selected_semester': selected_semester,
        'subjects': subjects,
        'class_subjects': class_subjects,
        'registered': registered,
    })
