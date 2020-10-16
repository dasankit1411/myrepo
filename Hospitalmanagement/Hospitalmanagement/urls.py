"""Hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Hospital import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.Aboutus,name='about'),
    path('contact/', views.Contact,name='contact'),
    path('', views.Index,name='home'),
    path('admin_login/', views.Login,name='login'),
    path('logout/', views.Logout,name='logout'),
    path('view_doctor/', views.View_doctor,name='view_doctor'),
    path('add_doctor/', views.Add_doctor,name='add_doctor'),
    path('add_patient/', views.Add_patient,name='add_patient'),
    path('delete_doctor(?P<int:pid>)', views.Delete_doctor,name='delete_doctor'),
    path('delete_patient(?P<int:sid>)', views.Delete_patient,name='delete_patient'),
    path('view_patient/', views.View_patient,name='view_patient'),
    path('add_appointment/', views.Add_appointment,name='add_appointment'),
    path('view_appointment/', views.View_appointment,name='view_appointment'),
    path('delete_appointment(?P<int:sid>)', views.Delete_appointment,name='delete_appointment'),

]
