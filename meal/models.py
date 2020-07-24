from django.db import models

class User(models.Model):
    objects = models.Manager()
    user_id = models.CharField(primary_key = True, max_length=200)
    user_pw = models.CharField(max_length=200)
    user_nick = models.CharField(max_length=100)
    user_email = models.CharField(max_length=500)
    user_last_kind = models.CharField(max_length = 500, default = "오점뭐!")
    user_last_name1 = models.CharField(max_length = 500, default = "오점뭐!")
    user_last_name2 = models.CharField(max_length = 500, default = "오점뭐!")
    user_last_name3 = models.CharField(max_length = 500, default = "오점뭐!")
    user_last_name4 = models.CharField(max_length = 500, default = "오점뭐!")
    user_last_name5 = models.CharField(max_length = 500, default = "오점뭐!")
    user_loc_x = models.FloatField()
    user_loc_y = models.FloatField()
    user_loc_add = models.CharField(max_length = 500, default = '우림라이온스밸리A')



