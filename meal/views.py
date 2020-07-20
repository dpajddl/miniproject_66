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
    return render(request, 'meal/random_lunch.html', {})

def mylocation(request):
    return render(request, 'meal/mylocation.html', {})

def signup(request):
    return render(request, 'meal/signup.html', {})

def something(request):
    return render(request, 'meal/something.html', {})

# Create your views here.
