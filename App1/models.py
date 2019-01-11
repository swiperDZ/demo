from django.db import models


class User(models.Model):

    """手机号，用户名，性别，出生年份，常住地，爱好，个人说明"""
    u_phone = models.CharField(max_length=16)
    u_username = models.CharField(max_length=32)
    u_sex = models.BooleanField()
    u_birth_year = models.IntegerField(max_length=4, null=True)
    u_location = models.CharField(max_length=64, null=True)
    u_hobby = models.CharField(max_length=64, null=True)
    u_instructions = models.CharField(max_length=128, null=True)


class UserProfile(models.Model):

    """ 用户ID，目标城市，最小查找范围，最大查找范围，最小交友年龄，
        最大交友年龄，匹配的性别，是否开启震动"""
    p_user_id = models.IntegerField()
    p_location = models.CharField(max_length=32)
    p_min_distance = models.IntegerField(max_length=1, default=5)
    p_max_distance = models.IntegerField(max_length=3, default=20)
    p_min_dating_age = models.IntegerField(default=15)
    p_max_dating_age = models.IntegerField(default=30)
    p_dating_Sex = models.BooleanField()
    p_vibration = models.BooleanField(default=True)