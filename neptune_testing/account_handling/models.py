from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# class UserType(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return "undefined user"


class User(AbstractUser):
    permission = models.CharField(max_length=100)


class Agent(User):
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Agent"


class Staff(User):
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Staff"


class Client(User):
    agent_company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Client"
