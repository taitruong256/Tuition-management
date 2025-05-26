from django.db import models
from accounts.models import StudentUser
from debt.models import PaymentHistory

class Invoice(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='invoices')
    payment = models.OneToOneField(PaymentHistory, on_delete=models.CASCADE, related_name='invoice')
    created_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='invoices/', blank=True, null=True, verbose_name='File hóa đơn (PDF)')

    def __str__(self):
        return f"Invoice #{self.id} - {self.student} - {self.payment.amount} VND"
