from django.db import models
from account_handling.models import User

class List(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    text = models.CharField(max_length=500, blank=True, null=True)
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
