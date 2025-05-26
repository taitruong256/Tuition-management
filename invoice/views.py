from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice
from debt.models import PaymentHistory
from django.http import FileResponse, Http404

# Create your views here.

@login_required
def my_invoices(request):
    invoices = Invoice.objects.filter(student=request.user).order_by('-created_at')
    return render(request, 'invoice/my_invoices.html', {'invoices': invoices})

@login_required
def download_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, student=request.user)
    if not invoice.pdf_file:
        raise Http404('Hóa đơn chưa có file đính kèm.')
    return FileResponse(invoice.pdf_file.open('rb'), as_attachment=True, filename=f'Invoice_{invoice.id}.pdf')
