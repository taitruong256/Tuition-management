from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    path('chuong-trinh-khung/', views.curriculum_framework_list, name='curriculum_framework_list'),
    path('chuong-trinh-khung/them/', views.curriculum_framework_create, name='curriculum_framework_create'),
    path('chuong-trinh-khung/<int:pk>/sua/', views.curriculum_framework_update, name='curriculum_framework_update'),
    path('chuong-trinh-khung/<int:pk>/xoa/', views.curriculum_framework_delete, name='curriculum_framework_delete'),
] 