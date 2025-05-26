"""
URL configuration for tuition_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('curriculum/', include('curriculum.urls', namespace='curriculum')),
    path('registration/', include('registration.urls', namespace='registration')),
    path('debt/', include('debt.urls', namespace='debt')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('admin/logout/', logout_view, name='admin_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
