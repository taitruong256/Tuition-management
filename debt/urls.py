from django.urls import path
from . import views

app_name = 'debt'

urlpatterns = [
    path('my-debt/', views.my_debt, name='my_debt'),
    path('my-debt-detail/', views.my_debt_detail, name='my_debt_detail'),
]