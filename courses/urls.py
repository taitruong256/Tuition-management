from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('register/', views.course_registration, name='course_registration'),
    path('register/submit/', views.register_course, name='register_course'),
]
