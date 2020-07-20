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
    path('meal/search_all/', views.search_all, name = 'search_all'),
    path('meal/something/', views.something, name = 'something'),
    path('meal/signup/', views.signup, name = 'signup'),
    path('', views.index_login, name = 'index_login'),
]
