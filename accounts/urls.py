from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.StudentLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.StudentPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.StudentPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.StudentPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.StudentPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('password-change/', views.StudentPasswordChangeView.as_view(), name='password_change'),
] 