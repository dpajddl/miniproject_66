from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from random import *
import json
from django.forms.models import model_to_dict
import simplejson,requests
import sys
from json import JSONEncoder
import requests
import bcrypt

def index_login(request):
    return render(request, 'meal/index_login.html', {})

def index(request):
    my_user = User.objects.get(user_id = request.session['user']['user_id'])
    last1 = my_user.user_last_name1
    last2 = my_user.user_last_name2
    last3 = my_user.user_last_name3
    last4 = my_user.user_last_name4
    last5 = my_user.user_last_name5
    return render(request, 'meal/index.html', {'last1' : last1, 'last2' : last2, 'last3' : last3, 'last4' : last4, 'last5' : last5, 'my_user' : my_user})

def search_all(request):
    # 페이징
    # 1 - 현재 페이지 정보 get
    page = request.GET.get('page')

    # 2 - page에 해당하는 식당의 (리스트 상의) 시작번호와 끝번호를 알아내기
    # startRow = 0
    # endRow = 0
    
    restaurant_all = request.session['rest']
    # restaurant_all = restaurant_all[0:10]

    return render(request, 'meal/search_all.html', {'restaurant_all' : restaurant_all})



def random_lunch(request):
    random_lunch = request.session['rest']
    user_all = User.objects.all()

    while(True) : 
        my_user = User.objects.get(user_id = request.session['user']['user_id'])
        i = randint(0, len(random_lunch)-1)
        pick = random_lunch[i]
        if my_user.user_last_kind == pick['id']:
            pass
        else :
            request.session['pick'] = pick
            return render(request, 'meal/random_lunch.html',
            {'pick' : pick})


def mylocation(request):
    my_user = User.objects.get(user_id = request.session['user']['user_id'])
    return render(request, 'meal/mylocation.html', {'my_user' : my_user})

def signup(request):
    return render(request, 'meal/signup.html', {})

def something(request):
    return render(request, 'meal/something.html', {})

def findid(request):
    return render(request, 'meal/findid.html', {})

def findpw(request):
    return render(request, 'meal/findpw.html', {})

def login_function(request) :
    ln = 0
    login_id = request.POST.get('login_id')
    login_pw = request.POST.get('login_pw')
    user_all = User.objects.all()
    for i in range(len(user_all)):
        if user_all[i].user_id == login_id:
            if bcrypt.checkpw(login_pw.encode('utf-8'), user_all[i].user_pw.encode('utf-8')):
                obj = model_to_dict(user_all[i])
                request.session['user'] = obj
                url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
                apikey = "0fd8917caae3b9798b5233596bbdd2e7"
                x = request.session['user']['user_loc_x']
                y = request.session['user']['user_loc_y']
                restaurant_all=[]
                r = requests.get( url, params = {'query':'식당',
                        'category_group_code':'FD6',
                    'x':x,
                    'y':y,
                    'radius':300}, headers={'Authorization' : 'KakaoAK ' + apikey } )
                obj=r.json()
                counts=obj['meta']['pageable_count']
                total_pages= counts//15 if counts%15 == 0 else counts //15+1
                for page in range(total_pages):
                    r = requests.get( url, params = {'query':'식당',
                        'category_group_code':'FD6',
                        'x': x,
                    'y':y,
                    'radius':300,'page':page+1}, headers={'Authorization' : 'KakaoAK ' + apikey } )
                    obj=r.json()
                    docs=obj['documents']
                    for doc in docs:
                        restaurant_all.append(doc)

                request.session['rest'] = restaurant_all
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
    signup_ad = request.POST.get('signup_ad')
    user_all = User.objects.all()
    signup_pw = signup_pw.encode('utf-8')   # 회원가입 시 입력된 패스워드를 바이트 형태로 인코딩    
    signup_pw_crypt = bcrypt.hashpw(signup_pw, bcrypt.gensalt())  # 암호화된 비밀번호 생성
    signup_pw_crypt = signup_pw_crypt.decode('utf-8')             # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩
    for i in range(len(user_all)):
        if user_all[i].user_id == signup_id:
            return HttpResponse('1')
            s_up = s_up + 1
    if s_up == 0:
        param = {'query': signup_ad}
        header = {'Authorization' : 'KakaoAK d4be7b479f4b4cbd99bd19ae87f88b4b'}
        req = requests.get('https://dapi.kakao.com/v2/local/search/keyword.json', params=param, headers=header)
        obj = req.json()
        docs = obj['documents']
        if docs == []:
            return HttpResponse('2')
        else :
            xx=docs[0]['x']
            yy=docs[0]['y']
            user_loc_x = xx
            user_loc_y = yy
        
        newbie = User(
            user_id=signup_id, user_pw=signup_pw_crypt,
            user_email=signup_email, user_nick = signup_nick,
            user_loc_x = user_loc_x, user_loc_y = user_loc_y)
        newbie.save();
        return HttpResponse('0')
    

# def last_kind_function(request) :
#     pick_kind = request.get('pick_kind')
#     request.session.user.user_last_kind = pick_kind
#     user.save()
#     return HttpResponse('0')

def mylocation_function(request) :
    my_user = User.objects.get(user_id = request.session['user']['user_id'])
    mylocation_ad = request.GET.get('mylocation_ad')
    param = {'query': mylocation_ad}
    header = {'Authorization' : 'KakaoAK d4be7b479f4b4cbd99bd19ae87f88b4b'}
    req = requests.get('https://dapi.kakao.com/v2/local/search/keyword.json', params=param, headers=header)
    obj = req.json()
    docs = obj['documents']
    if docs == []:
        return HttpResponse('1')
    else :
        xx=docs[0]['x']
        yy=docs[0]['y']
        my_user.user_loc_x = xx
        my_user.user_loc_y = yy
        my_user.save()
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
        apikey = "0fd8917caae3b9798b5233596bbdd2e7"
        x = my_user.user_loc_x
        y = my_user.user_loc_y
        restaurant_all=[]
        r = requests.get( url, params = {'query':'식당',
                'category_group_code':'FD6',
            'x':x,
            'y':y,
            'radius':300}, headers={'Authorization' : 'KakaoAK ' + apikey } )
        obj=r.json()
        counts=obj['meta']['pageable_count']
        total_pages= counts//15 if counts%15 == 0 else counts //15+1
        for page in range(total_pages):
            r = requests.get( url, params = {'query':'식당',
                'category_group_code':'FD6',
                'x': x,
            'y':y,
            'radius':300,'page':page+1}, headers={'Authorization' : 'KakaoAK ' + apikey } )
            obj=r.json()
            docs=obj['documents']
            for doc in docs:
                restaurant_all.append(doc)

                request.session['rest'] = restaurant_all
        return HttpResponse('0')

def having_function(request):
    last_name = request.session['pick']['place_name']
    last_kind = request.session['pick']['id']
    my_user = User.objects.get(user_id = request.session['user']['user_id'])
    my_user.user_last_name5 = my_user.user_last_name4
    my_user.user_last_name4 = my_user.user_last_name3
    my_user.user_last_name3 = my_user.user_last_name2
    my_user.user_last_name2 = my_user.user_last_name1
    my_user.user_last_name1 = last_name
    my_user.user_last_kind = last_kind
    my_user.save()
    return HttpResponse('0')

def findid_function(request):
    findid_nick = request.POST.get('findid_nick')
    findid_email = request.POST.get('findid_email')
    
    # 해당 데이터만 조회
    try:
        user = User.objects.get(user_nick=findid_nick, user_email=findid_email)
        return JsonResponse(model_to_dict(user), safe=False)
        # return render(request, 'meal/findid.html', {'user':user_all[i]}) 
    except:
        return JsonResponse({'result':'fail'}, safe=False)

def findpw_function(request):
    findpw_nick = request.POST.get('findpw_nick')
    findpw_email = request.POST.get('findpw_email')
    findpw_id = request.POST.get('findpw_id')

    # 해당 데이터만 조회
    try:
        user = User.objects.get(user_nick=findpw_nick, user_email=findpw_email, user_id = findpw_id)
        user=model_to_dict(user)
        return JsonResponse(user, safe=False)
    except:
        return JsonResponse({'result':'fail'}, safe=False)

def changepw_function(request):
    change_pw = request.POST.get('change_pw')
    myuser = request.POST.get('user')
    print(myuser)
    user_id = User.objects.get(user_id = myuser['user_id'])
    change_pw = change_pw.encode('utf-8')   # 회원가입 시 입력된 패스워드를 바이트 형태로 인코딩    
    change_pw_crypt = bcrypt.hashpw(change_pw, bcrypt.gensalt())  # 암호화된 비밀번호 생성
    change_pw_crypt = change_pw_crypt.decode('utf-8')             # DB에 저장할 수 있는 유니코드 문자열 형태로 디코딩
    user.user_pw = change_pw
    user.save()
    return HttpResponse('0')


