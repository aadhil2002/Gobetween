"""gobetween URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

from gobetween_app.views import driver_registartion, login_view,user_registration,comp_registration,IndexView,about,contact

from gobetween_app import freelance_driver_urls, user_urls,admin_urls,driver_urls,company_urls

urlpatterns = [
    path('', IndexView.as_view()),
    path('login_view',login_view.as_view()),
    path('user_reg',user_registration.as_view()),
    path('driver_reg',driver_registartion.as_view()),
    path('comp_reg',comp_registration.as_view()),
    path('user/',user_urls.urls()),
    path('admin/',admin_urls.urls()),
    path('driver/',driver_urls.urls()),
    path('freelance_driver/',freelance_driver_urls.urls()),
    path('company/',company_urls.urls()),
    path('about',about.as_view()),
    path('contact',contact.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
