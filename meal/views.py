from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from random import *
import json
from django.forms.models import model_to_dict

from json import JSONEncoder

def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    return render(request, 'meal/index.html', {})

def search_all(request):
    restaurant_all = Restaurant.objects.all()
    rest_kind_all = Rest_kind.objects.all()
    return render(request, 'meal/search_all.html', {'rest_kind_all' : rest_kind_all,'restaurant_all' : restaurant_all})

def random_lunch(request):
    restaurant_all = Restaurant.objects.all()
    rest_kind_all = Rest_kind.objects.all()
    user_all = User.objects.all()
    i = randint(0, len(restaurant_all)-1)
    pick = restaurant_all[i]
    return render(request, 'meal/random_lunch.html',
     {'restaurant_all' : restaurant_all, 'rest_kind_all' : rest_kind_all, 'pick' : pick})

def random_lunch(request):
    
    restaurant_all = Restaurant.objects.all()
    rest_kind_all = Rest_kind.objects.all()
    user_all = User.objects.all()
    i = randint(0, len(restaurant_all)-1)
    pick = restaurant_all[i]
    
    
    return render(request,'meal/random_lunch.html',
     {'restaurant_all' : restaurant_all, 'rest_kind_all' : rest_kind_all, 'pick' : pick})     

def mylocation(request):
    return render(request, 'meal/mylocation.html', {})

def signup(request):
    return render(request, 'meal/signup.html', {})

def something(request):
    return render(request, 'meal/something.html', {})

def login_function(request) :
    login_id = request.POST.get('login_id')
    login_pw = request.POST.get('login_pw')
    user_all = User.objects.all()
    for i in range(len(user_all)):
        if user_all[i].user_id == login_id:
            if user_all[i].user_pw == login_pw:
                obj = model_to_dict(user_all[i])
                request.session['user'] = obj
                return HttpResponse('0')
            else :
                return HttpResponse('1')
        else :
            return HttpResponse('2')
# Create your views here.
