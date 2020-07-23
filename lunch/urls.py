"""lunch URL Configuration

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
from django.urls import path, include
from meal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', views.index, name = 'index'),
    path('meal/mylocation/', views.mylocation, name = 'mylocation'),
    path('meal/random_lunch/', views.random_lunch, name = 'random_lunch'),
    path('random_lunch_again/', views.random_lunch, name = 'random_lunch_again'),
    path('meal/search_all/', views.search_all, name = 'search_all'),
    path('meal/something/', views.something, name = 'something'),
    path('meal/signup/', views.signup, name = 'signup'),
    path('meal/findid/', views.findid, name = 'findid'),
    path('meal/findpw/', views.findpw, name = 'findpw'),
    path('', views.index_login, name = 'index_login'),
    path('login_function/', views.login_function, name = 'login_function'),
    path('signup_function/', views.signup_function, name = 'signup_function'),
    path('mylocation_function/', views.mylocation_function, name = 'mylocation_function'),
    path('having_function/', views.having_function, name = 'having_function'),
    path('findid_function/', views.findid_function, name = 'findid_function'),
    path('findpw_function/', views.findpw_function, name = 'findpw_function'),
    path('changepw_function/', views.changepw_function, name = 'changepw_function'),
]
