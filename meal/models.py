from django.db import models

class User(models.Model):
    objects = models.Manager()
    user_id = models.CharField(primary_key = True, max_length=200)
    user_pw = models.CharField(max_length=200)
    user_nick = models.CharField(max_length=100)
    user_email = models.CharField(max_length=500)
    user_last_kind = models.CharField(max_length = 500)
    user_loc_x = models.FloatField()
    user_loc_y = models.FloatField()




