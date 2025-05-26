from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OnlinePaymentForm
from .models import OnlinePayment
from debt.models import TuitionDebt, OtherFee
from registration.models import Registration

# Create your views here.

@login_required
def pay_tuition(request):
    # Lấy tất cả các đăng ký môn học thuộc các học kỳ có công nợ chưa thanh toán
    unpaid_debts = TuitionDebt.objects.filter(student=request.user, status='unpaid')
    unpaid_semester_ids = unpaid_debts.values_list('semester_id', flat=True)
    unpaid_regs = Registration.objects.filter(student=request.user, class_subject__subject__semester_id__in=unpaid_semester_ids)
    unpaid_subjects = []
    for reg in unpaid_regs.select_related('class_subject__subject'):
        subject = reg.class_subject.subject
        amount = subject.theory_credits * 700_000 + subject.practice_credits * 1_000_000
        unpaid_subjects.append({
            'id': reg.id,
            'semester_id': subject.semester_id,
            'subject': subject,
            'credits': subject.credits,
            'theory_credits': subject.theory_credits,
            'practice_credits': subject.practice_credits,
            'amount': amount,
            'registered_at': reg.registered_at,
        })
    # Lấy các khoản thu khác chưa thanh toán
    unpaid_other = OtherFee.objects.filter(student=request.user, status='unpaid')
    if request.method == 'POST':
        reg_ids = request.POST.get('tuition_ids', '').split(',')
        other_ids = request.POST.get('other_ids', '').split(',')
        total_amount = int(request.POST.get('total_amount', 0))
        # Cập nhật trạng thái TuitionDebt của các học kỳ có môn được chọn sang 'pending'
        if reg_ids and reg_ids != ['']:
            semesters = Registration.objects.filter(id__in=reg_ids).values_list('class_subject__subject__semester_id', flat=True).distinct()
            TuitionDebt.objects.filter(student=request.user, semester_id__in=semesters, status='unpaid').update(status='pending')
        if other_ids and other_ids != ['']:
            OtherFee.objects.filter(id__in=other_ids, student=request.user).update(status='pending')
        momo_response = {"payUrl": "https://momo.vn/redirect/payment-demo"}
        return render(request, 'payment/payment_submitted.html', {
            'total_amount': total_amount,
            'momo_url': momo_response['payUrl'],
        })
    else:
        form = OnlinePaymentForm()
    return render(request, 'payment/pay_tuition.html', {
        'form': form,
        'unpaid_tuition': unpaid_subjects,
        'unpaid_other': unpaid_other,
    })
