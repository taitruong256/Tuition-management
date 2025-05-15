from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('make/', views.make_payment, name='make_payment'),
    path('make/<str:student_id>/', views.make_payment, name='make_payment_for_student'),
    path('detail/<str:receipt_number>/', views.payment_detail, name='payment_detail'),
    path('process/<int:payment_id>/', views.process_payment, name='process_payment'),
]