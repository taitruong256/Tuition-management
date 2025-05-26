from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OnlinePaymentForm
from .models import OnlinePayment
from debt.models import TuitionDebt, OtherFee

# Create your views here.

@login_required
def pay_tuition(request):
    # Lấy các khoản học phí và khoản thu khác chưa thanh toán của sinh viên
    unpaid_tuition = TuitionDebt.objects.filter(student=request.user, status='unpaid')
    unpaid_other = OtherFee.objects.filter(student=request.user, status='unpaid')
    if request.method == 'POST':
        tuition_ids = request.POST.getlist('tuition_ids')
        other_ids = request.POST.getlist('other_ids')
        total_amount = int(request.POST.get('total_amount', 0))
        # Gọi API MoMo ở đây với total_amount
        momo_response = {"payUrl": "https://momo.vn/redirect/payment-demo"}
        return render(request, 'payment/payment_submitted.html', {
            'total_amount': total_amount,
            'momo_url': momo_response['payUrl'],
        })
    else:
        form = OnlinePaymentForm()
    return render(request, 'payment/pay_tuition.html', {
        'form': form,
        'unpaid_tuition': unpaid_tuition,
        'unpaid_other': unpaid_other,
    })
