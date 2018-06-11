from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def type(self):
        return 'undefined'


class Agent(UserType):
    company = models.CharField(max_length=30, blank=True)

    @property
    def type(self):
        return 'Agent'

class Staff(UserType):

    @property
    def type(self):
        return 'Staff'

class Client(UserType):
    agent_company = models.CharField(max_length=30, blank=True)

    @property
    def type(self):
        return 'Client'
