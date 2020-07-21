from django.db import models

class Rest_kind(models.Model):
    res_kind_num = models.IntegerField(primary_key = True)
    res_kind_name = models.CharField(max_length=200)

class Restaurant(models.Model) :
    ##이거는 크롤링해서 바로 가져올 수 있는 친구들로 구성!
    rest_num = models.IntegerField(primary_key=True) #카카오에서 제공하는 id가 있다.
    rest_name = models.CharField(max_length=500)
    rest_star = models.FloatField()
    rest_address = models.CharField(max_length=500)
    rest_time = models.CharField(max_length=100)
    rest_tele = models.CharField(max_length=100)
    rest_review = models.IntegerField()
    rest_kind_num = models.ForeignKey(Rest_kind, on_delete=models.CASCADE) #kind_num으로 먹었던거 안먹는 로직 구현
    rest_detail_link = models.CharField(max_length=500) #상세보기 링크
    ##회원정보에서 가져온다.

class User(models.Model):
    objects = models.Manager()
    user_number = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_nick = models.CharField(max_length=100)
    user_email = models.CharField(max_length=500)
    user_last_kind = models.ForeignKey(Rest_kind, on_delete=models.CASCADE, default = 1)
    uesr_loc_x = models.FloatField(default = 100)
    uesr_loc_y = models.FloatField(default = 100)
    # def __init__(self, user_number = user_number, user_id=user_id, user_pw=user_pw, user_nick=user_nick, user_email = user_email, user_last_kind = user_last_kind, uesr_loc_x = uesr_loc_x, uesr_loc_y = uesr_loc_y):
    #     self.user_number = user_number
    #     self.user_id = user_id
    #     self.user_pw = user_pw
    #     self.user_nick = user_nick
    #     self.user_email = user_email
    #     self.user_last_kind = user_last_kind
    #     self.uesr_loc_x = uesr_loc_x
    #     self.uesr_loc_y = uesr_loc_y

    #user_craw_up = models.DateField(default = )
    



