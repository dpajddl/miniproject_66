from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant
from random import *

def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    return render(request, 'meal/index.html', {})

def search_all(request):
    return render(request, 'meal/search_all.html', {})

def random_lunch(request):
    r_list = Restaurant.objects.all()

    return render(request, 'meal/random_lunch.html', {"r_list" : r_list})

def mylocation(request):
    return render(request, 'meal/mylocation.html', {})

def signup(request):
    return render(request, 'meal/signup.html', {})

def something(request):
    return render(request, 'meal/something.html', {})

# Create your views here.
