from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    path('chuong-trinh-khung/', views.curriculum_framework_list, name='curriculum_framework_list'),
] 