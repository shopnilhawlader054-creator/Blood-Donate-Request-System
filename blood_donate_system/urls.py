"""
URL configuration for blood_donate_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from blood.views import home,register,login,donor_request,creat_donor,view_donor_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=home,name='home'),
    path('register/',view=register,name='register'),
    path('login/',view=login,name='login'),
    path('creatdonor/',view=creat_donor,name='creat_donor'),
    path('donorrequest/<int:pk>/',view=donor_request,name='donor_request'),
    path('donorprofile/',view=view_donor_profile,name='view_donor_profile')
]
