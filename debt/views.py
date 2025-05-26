# debt/utils.py
from registration.models import Registration
from django.contrib.auth.decorators import login_required
from .models import TuitionDebt, OtherFee, PaymentHistory
from django.shortcuts import render
from curriculum.models import Semester
from django.db.models import Sum

def update_tuition_debt_for_student(student, semester):
    regs = Registration.objects.filter(
        student=student,
        class_subject__subject__semester=semester
    )
    theory_credits = sum(
        reg.class_subject.subject.theory_credits
        for reg in regs if reg.class_subject.type == 'LT'
    )
    practice_credits = sum(
        reg.class_subject.subject.practice_credits
        for reg in regs if reg.class_subject.type == 'TH'
    )
    debt, created = TuitionDebt.objects.get_or_create(
        student=student, semester=semester,
        defaults={'theory_credits': theory_credits, 'practice_credits': practice_credits}
    )
    if not created:
        debt.theory_credits = theory_credits
        debt.practice_credits = practice_credits
        debt.save()
    return debt

@login_required
def my_debt(request):
    from registration.models import Registration
    from curriculum.models import Semester
    from debt.models import TuitionDebt

    # Lấy tất cả đăng ký của sinh viên, kèm theo thông tin học kỳ
    regs = Registration.objects.filter(student=request.user).select_related(
        'class_subject__subject__semester'
    )
    # Gom các đăng ký theo học kỳ
    semester_map = {}
    for reg in regs:
        semester = reg.class_subject.subject.semester
        if semester not in semester_map:
            semester_map[semester] = []
        semester_map[semester].append(reg)
    # Chuẩn bị dữ liệu cho template
    semester_data = []
    for semester, regs in sorted(semester_map.items(), key=lambda x: x[0].order, reverse=True):
        subject_rows = []
        total_credits = 0
        total_amount = 0
        # Lấy trạng thái công nợ của học kỳ này
        debt = TuitionDebt.objects.filter(student=request.user, semester=semester).first()
        debt_status = debt.get_status_display() if debt else 'Chưa thanh toán'
        for reg in regs:
            subject = reg.class_subject.subject
            credits = subject.credits
            amount = subject.theory_credits * 700_000 + subject.practice_credits * 1_000_000
            subject_rows.append({
                'subject': subject,
                'class_subject': reg.class_subject,
                'credits': credits,
                'theory_credits': subject.theory_credits,
                'practice_credits': subject.practice_credits,
                'amount': amount,
                'registered_at': reg.registered_at,
                'debt_status': debt_status,
            })
            total_credits += credits
            total_amount += amount
        semester_data.append({
            'semester': semester,
            'subjects': subject_rows,
            'total_credits': total_credits,
            'total_amount': total_amount,
        })
    # Các khoản thu khác
    other_fees = OtherFee.objects.filter(student=request.user)
    payment_history = PaymentHistory.objects.filter(student=request.user).order_by('-paid_at')
    return render(request, 'debt/my_debt.html', {
        'semester_data': semester_data,
        'other_fees': other_fees,
        'payment_history': payment_history,
    })

@login_required
def my_debt_detail(request):
    # Lấy tất cả học kỳ mà sinh viên đã đăng ký
    semesters = Semester.objects.filter(subjects__class_subjects__registrations__student=request.user).distinct().order_by('-order')
    semester_data = []
    for semester in semesters:
        # Lấy các đăng ký của sinh viên trong học kỳ này
        regs = Registration.objects.filter(
            student=request.user,
            class_subject__subject__semester=semester
        ).select_related('class_subject__subject')
        # Gom theo môn học
        subject_rows = []
        total_credits = 0
        total_amount = 0
        for reg in regs:
            subject = reg.class_subject.subject
            credits = subject.credits
            # Tính học phí từng môn
            amount = subject.theory_credits * 700_000 + subject.practice_credits * 1_000_000
            subject_rows.append({
                'subject': subject,
                'class_subject': reg.class_subject,
                'credits': credits,
                'theory_credits': subject.theory_credits,
                'practice_credits': subject.practice_credits,
                'amount': amount,
                'registered_at': reg.registered_at,
            })
            total_credits += credits
            total_amount += amount
        semester_data.append({
            'semester': semester,
            'subjects': subject_rows,
            'total_credits': total_credits,
            'total_amount': total_amount,
        })
    return render(request, 'debt/my_debt_detail.html', {
        'semester_data': semester_data,
    })