from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)

    def __str__(self):
        return  self.name