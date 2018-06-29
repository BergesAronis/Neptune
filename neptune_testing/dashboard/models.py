from django.db import models
from account_handling.models import User

# Create your models here.
class Navigation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    permission = models.PositiveIntegerField()

    def __str__(self):
        return self.name
