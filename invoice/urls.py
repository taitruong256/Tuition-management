from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('my/', views.my_invoices, name='my_invoices'),
    path('download/<int:invoice_id>/', views.download_invoice, name='download_invoice'),
] 