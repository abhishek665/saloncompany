"""salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('service/<str:service>/<int:uid>/', views.services),
    path('select/<str:service>/<int:service_uid>/<str:sub_name>/<int:sub_uid>/', views.select),
    path('checkout/', views.checkout),
    path('my_orders/', views.my_orders),
    path('send_otp/', views.send_otp),
    path('success/', views.success),
]
