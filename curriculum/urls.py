from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    path('', views.curriculum_list, name='list'),
    path('<int:pk>/', views.curriculum_detail, name='detail'),
    path('my/', views.my_curriculum, name='my_curriculum'),
] 