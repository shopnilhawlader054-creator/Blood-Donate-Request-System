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
from blood.views import home,register,login,donor_request,creat_donor,view_donor_profile,all_petient,delete_donar_acount,edit_donor_aocunt,user_logout,donor_detals,petient_detals,my_request,edit_my_request,delet_blood_request,filter_donor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=home,name='home'),
    path('register/',view=register,name='register'),
    path('login/',view=login,name='login'),
    path('creatdonor/',view=creat_donor,name='creat_donor'),
    path('donorrequest/<int:pk>/',view=donor_request,name='donor_request'),
    path('donorprofile/',view=view_donor_profile,name='view_donor_profile'),
    path('delet_donor/<int:pk>/',view=delete_donar_acount,name='delete_donar_acount'),
    path('editdonor/<int:pk>/',view=edit_donor_aocunt,name='edit_donor_aocunt'),
    path('logout/',view=user_logout,name='user_logout'),
    path('allpetient/',view=all_petient,name='all_petient'),
    path('donordetals/<int:pk>/',view=donor_detals,name='donor_detals'),
    path('petientdetals/<int:pk>/',view=petient_detals,name='petient_detals'),
    path('myrequest/',view=my_request,name='my_request'),
    path('editmyrequest/<int:pk>/',view=edit_my_request,name="edit_my_request"),
    path('deletbloodrequest/<int:pk>/',view=delet_blood_request,name='delet_blood_request'),
    path('filterdonor/',view=filter_donor,name='filter_donor')
]
