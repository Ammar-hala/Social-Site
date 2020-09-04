"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , include
from . import views # grab views from current directory

urlpatterns = [
    path('' , views.HomePage.as_view() , name='home'),
    path('accounts/' , include('accounts.urls' , namespace='accounts')) , #find what namespace is for?
    path('accounts/' , include('django.contrib.auth.urls') ) , # connects everything django has related to authorization to accounts app
    # no need to register any models in admin of accounts as using django's builtin user models.. so no need to register anythign in accounts admin
    path('test/' , views.TestPage.as_view() , name='test'),  # for loggin in page
    path('thanks/' , views.ThanksPage.as_view() , name='thanks'), # logging out page

    path('posts/' , include('posts.urls' , namespace='posts') ) ,
    path('groups/' , include('groups.urls' , namespace='groups') ) , 

    path('admin/', admin.site.urls),
]
