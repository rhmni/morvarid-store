import os
from datetime import datetime
from random import randint

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


def upload_avatar_user(instance, filename):
    filename = os.path.basename(filename)
    filebase, extension = filename.rsplit('.', maxsplit=1)
    number = randint(1000, 9999)
    return f'{instance.email}[{number}].{extension}'


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError('plaese enter valid email')
        if not first_name:
            raise ValueError('plaese enter first name')
        if not last_name:
            raise ValueError('plaese enter last name')
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=150, unique=True, verbose_name='آدرس ایمیل')
    phone = models.CharField(max_length=11, verbose_name='موبایل', null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_avatar_user, default="default_avatar.jpg", verbose_name='تصویر',
                               null=True, blank=True)
    # receiver information
    code_meli = models.CharField(max_length=10, verbose_name='کد ملی', null=True, blank=True)
    ostan = models.CharField(max_length=50, verbose_name='استان', null=True, blank=True)
    shahr = models.CharField(max_length=70, verbose_name='شهر', null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    join_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ ثبت نام')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_superuser = models.BooleanField(default=False, verbose_name='ادمین')
    USERNAME_FIELD = 'email'
    # this is for create super user in terminal
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
