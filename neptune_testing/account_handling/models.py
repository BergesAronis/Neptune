from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
