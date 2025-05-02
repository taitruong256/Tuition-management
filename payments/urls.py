from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('make/<str:student_id>/', views.make_payment, name='make_payment'),
    path('detail/<str:receipt_number>/', views.payment_detail, name='payment_detail'),
]