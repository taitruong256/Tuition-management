from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('pay-tuition/', views.pay_tuition, name='pay_tuition'),
]
