# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class UsersUser(AbstractBaseUser):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=254, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=14)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField()
    token = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_admin = models.BooleanField()
    avatar = models.CharField(max_length=100, blank=True, null=True)
    auto_deactivate = models.BooleanField()
    last_connection_date = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'cpf'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        managed = False
        db_table = 'users_user'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('remote_users.UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'