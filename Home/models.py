from django.db import models


# Create your models here.


class UserINFO(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

