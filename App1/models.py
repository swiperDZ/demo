import datetime
from django.db import models


class User(models.Model):
    """手机号，用户名，性别，出生年份，常住地，爱好，个人说明"""
    SEX = (
        ('male', '男性'),
        ('female', '女性'),
    )
    u_phone = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    u_username = models.CharField(max_length=32, unique= True, verbose_name='昵称')
    u_sex = models.CharField(max_length=8, verbose_name='性别', choices=SEX)
    u_birth_year = models.IntegerField(max_length=8, default=2000,
                                       verbose_name='出生年')
    u_birth_month = models.IntegerField(max_length=8, default=1,
                                       verbose_name='出生月')
    u_birth_day = models.IntegerField(max_length=4, default=1,
                                       verbose_name='出生日')
    u_location = models.CharField(max_length=64, null=True, verbose_name='常住地')
    u_hobby = models.CharField(max_length=64, null=True, verbose_name='爱好')
    u_instructions = models.CharField(max_length=128, null=True, verbose_name='个人说明')
    u_is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    u_token = models.IntegerField(default=60*60*24*15, null=True, verbose_name='token')
    u_icon = models.CharField(max_length=256, null=True, verbose_name='头像')

    class Meta:
        db_table = "user"

    @property
    def age(self):
        to_day = datetime.date.today()
        birth_date = datetime.date(self.u_birth_year, self.u_birth_month,
                                   self.u_birth_day)
        return (to_day - birth_date).days // 365

    def to_dict(self):
        return {
            "phone": self.u_phone,
            "username": self.u_username,
            "sex": self.u_sex,
            "age": self.age,
            "location": self.u_location,
            "hobby": self.u_hobby
        }


class UserProfile(models.Model):

    """ 用户ID，目标城市，最小查找范围，最大查找范围，最小交友年龄，
        最大交友年龄，匹配的性别，是否开启震动"""
    p_user_id = models.ForeignKey(User)
    p_location = models.CharField(max_length=32)
    p_min_distance = models.IntegerField(max_length=1, default=5)
    p_max_distance = models.IntegerField(max_length=3, default=20)
    p_min_dating_age = models.IntegerField(default=15)
    p_max_dating_age = models.IntegerField(default=30)
    p_dating_Sex = models.BooleanField()
    p_vibration = models.BooleanField(default=True)

    class Meta:
        db_table = "user_profile"