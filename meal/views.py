from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from random import *

def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    return render(request, 'meal/index.html', {})

def search_all(request):
    return render(request, 'meal/search_all.html', {})

def random_lunch(request):
    restaurant_all = Restaurant.objects.all()
    rest_kind_all = Rest_kind.objects.all()
    user_all = User.objects.all()
    i = randint(0, len(restaurant_all)-1)
    pick = restaurant_all[i]
    return render(request, 'meal/random_lunch.html',
     {'restaurant_all' : restaurant_all, 'rest_kind_all' : rest_kind_all, 'pick' : pick})

def mylocation(request):
    return render(request, 'meal/mylocation.html', {})

def signup(request):
    return render(request, 'meal/signup.html', {})

def something(request):
    return render(request, 'meal/something.html', {})

# Create your views here.
