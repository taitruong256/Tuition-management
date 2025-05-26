from django.contrib import admin
from .models import TuitionDebt, OtherFee, PaymentHistory

from django.shortcuts import render, redirect
from .forms import OtherFeeForm
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def add_other_fee(request):
    if request.method == 'POST':
        form = OtherFeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debt:other_fee_list')
    else:
        form = OtherFeeForm()
    return render(request, 'debt/add_other_fee.html', {'form': form})

@admin.register(TuitionDebt)
class TuitionDebtAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'theory_credits', 'practice_credits', 'total_amount', 'status')
    list_filter = ('semester', 'status')
    search_fields = ('student__full_name', 'student__student_id')

@admin.register(OtherFee)
class OtherFeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'name', 'amount', 'status')
    list_filter = ('semester', 'status', 'name')
    search_fields = ('student__full_name', 'student__student_id', 'name')

@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'amount', 'payment_type', 'description', 'paid_at')
    list_filter = ('semester', 'payment_type')
    search_fields = ('student__full_name', 'description')