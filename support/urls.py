from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
] 