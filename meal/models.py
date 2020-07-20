from django.db import models

class Rest_kind(models.Model):
    res_kind_num = models.IntegerField(primary_key = True)
    res_kind_name = models.CharField(max_length=200)

class Restaurant(models.Model) :
    ##이거는 크롤링해서 바로 가져올 수 있는 친구들로 구성!
    rest_num = models.IntegerField(default = -2) #카카오에서 제공하는 id가 있다.
    rest_name = models.CharField(max_length=500)
    rest_star = models.IntegerField(default = -3)
    rest_address = models.CharField(max_length=500)
    rest_kind_name = models.ForeignKey(Rest_kind,on_delete=models.CASCADE) #kind_name으로 먹었던거 안먹는 로직 구현
    rest_detail_link = models.CharField(max_length=500) #상세보기 링크
    ##회원정보에서 가져온다.

class User(models.Model):
    user_number = models.IntegerField(primary_key=True, default = -1)
    user_id = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_nick = models.CharField(max_length=100, default = "이름없는 손님")
    user_email = models.CharField(max_length=500, default = "xxxxx@xxxx.xxx")
    user_last_kind = models.ForeignKey(Rest_kind, on_delete=models.CASCADE)
    uesr_loc_x = models.FloatField(default = 0)
    uesr_loc_y = models.FloatField(default = 0)
    #user_craw_up = models.DateField(default = )
    



