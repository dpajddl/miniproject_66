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

user_list = {}


def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    return render(request, 'meal/index.html', {})

def search_all(request):
  
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
    apikey = "0fd8917caae3b9798b5233596bbdd2e7"
    x = request.session['user']['uesr_loc_x']
    y = request.session['user']['uesr_loc_y']
    restaurant_all=[]
    r = requests.get( url, params = {'query':'식당',
            'category_group_code':'FD6',
        'x':x,
        'y':y,
        'radius':300}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    obj=r.json()
    print(obj)

    counts=obj['meta']['pageable_count']
    total_pages= counts//15 if counts%15 == 0 else counts //15+1
    print(total_pages)

    for page in range(total_pages):
        print(page+1)
        r = requests.get( url, params = {'query':'식당',
            'category_group_code':'FD6',
            'x':'126.966256146762',
        'y':'37.4775084271547',
        'radius':300,'page':page+1}, headers={'Authorization' : 'KakaoAK ' + apikey } )
        obj=r.json()
        docs=obj['documents']
        for doc in docs:
            restaurant_all.append(doc)
        


    request.session['rest'] = restaurant_all
    print(request.session['rest'])
    return render(request, 'meal/search_all.html', {'restaurant_all' : restaurant_all})



def random_lunch(request):
    random_lunch = request.session['rest']
    print('='*10)
    print(random_lunch)
    print('='*10)

    user_all = User.objects.all()
    i = randint(0, len(random_lunch)-1)
    pick = random_lunch[i]

    return render(request, 'meal/random_lunch.html',
     {'pick' : pick})


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
    import requests
    s_up = 0
    signup_id = request.POST.get('signup_id')
    signup_pw = request.POST.get('signup_pw')
    signup_email = request.POST.get('signup_email')
    signup_nick = request.POST.get('signup_nick')
    signup_ad = request.POST.get('signup_ad')
    user_all = User.objects.all()
    for i in range(len(user_all)):
        if user_all[i].user_id == signup_id:
            return HttpResponse('1')
            s_up = s_up + 1
        param = {'query': signup_ad}
        header = {'Authorization' : 'KakaoAK d4be7b479f4b4cbd99bd19ae87f88b4b'}

        req = requests.get('https://dapi.kakao.com/v2/local/search/address.json', params=param, headers=header)
        obj = req.json()
        docs = obj['documents']
        #add=obj['address']
        print(docs)
        for doc in docs:
            x=doc['address']['x']
            y=doc['address']['y']
            print(x,y)
        user_loc_x = x
        user_loc_y = y
    if s_up == 0:

        newbie = User(
            user_id=signup_id, user_pw=signup_pw,
            user_email=signup_email, user_nick = signup_nick,
            uesr_loc_x = user_loc_x, uesr_loc_y = user_loc_y)
        newbie.save();
        return HttpResponse('0')
    

def last_kind_function(request) :
    pick_kind = request.get('pick_kind')
    request.session.user.user_last_kind = pick_kind
    user.save()
    return HttpResponse('0')


# Create your views here.
