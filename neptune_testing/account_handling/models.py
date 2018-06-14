from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Agent(UserType):
    company = models.CharField(max_length=100, blank=True, null=True)


class Staff(UserType):
    company = models.CharField(max_length=100, blank=True, null=True)


class Client(UserType):
    company = models.CharField(max_length=100, blank=True, null=True)
