from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from random import *
import json
from django.forms.models import model_to_dict
import simplejson,requests
import sys
from json import JSONEncoder

def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    return render(request, 'meal/index.html', {})

def search_all(request):

    url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
    apikey = "0fd8917caae3b9798b5233596bbdd2e7"
    x=126.88263620024
    y=37.479966429878
    
    r = requests.get( url, params = {'query':'점심',
            'category_group_code':'FD6',
        'x':x,
        'y':y,
        'radius':300}, headers={'Authorization' : 'KakaoAK ' + apikey } )


    obj=r.json()
    counts=obj['meta']['total_count']
    total_pages= counts//15 if counts%15 == 0 else counts //15+1
    



    restaurant_all=obj['documents']

    return render(request, 'meal/search_all.html', {'restaurant_all' : restaurant_all})

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
    ln = 0
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
            ln = 1
    if ln == 0:
        return HttpResponse('2')

def signup_function(request) :
    s_up = 0
    signup_id = request.POST.get('signup_id')
    signup_pw = request.POST.get('signup_pw')
    signup_email = request.POST.get('signup_email')
    signup_nick = request.POST.get('signup_nick')
    user_all = User.objects.all()
    for i in range(len(user_all)):
        if user_all[i].user_id == signup_id:
            return HttpResponse('1')
            s_up = s_up + 1
    if s_up == 0:
        newbie = User(
            user_id=signup_id, user_pw=signup_pw,
            user_email=signup_email, user_nick = signup_nick)
        newbie.save();
        return HttpResponse('0')

# Create your views here.
