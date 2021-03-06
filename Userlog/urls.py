"""DjangoWebsite URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [

    path('nav', views.index, name='nav'),
    path('customer/<str:pk_test>/',views.customer_page, name="customer"),
    path('', views.home, name = "home"),
    path('welcome/', views.welcome),
    path('Userlogs/', views.topic_view, name = "logs"),
    path('entry/',views.user_list_view, name = "entry"),
    url('topics/$', views.topic_view, name='topics'),
    path('new_post/',views.createNew_post, name = "new_post"),
    path('update_post/<str:pk>/',views.update_post, name = "update_post"),
    path('delete_post/<str:pk>/',views.delete_post, name = "delete_post"),
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register"),

  #create path for newtopic model
]

#defining out functions

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('Userlog.urls', namespace= 'Userlog')),
]
"""


