"""
URL configuration for ptmprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ptmapp.views import register,login,drpdwn,home,cie,gpa,attendance,notification_list,save_response,parent_response_form







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',register),
    path('login/',login,name="login"),
    path('register/',register,name="register"),
    path('drpdwn/',drpdwn,name="drpdwn"),
    path('home/',home,name="home"),
    path('attendance/',attendance,name="attendance"),
    path('cie/',cie),
    path('gpa/',gpa),
    path('notifications/', notification_list, name='notification_list'),
    path('respond-notification-form/', parent_response_form, name='parent_response_form'),
    
    path('save-response/', save_response, name='save_response'),
   

]
