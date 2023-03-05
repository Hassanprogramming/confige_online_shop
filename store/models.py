from django.db import models
from blog.models import Admin
# Create your models here.

#This is for showing something at the begining of the page of Home and shop
class Website(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    header_title = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(max_length=300, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class About(models.Model):
    text = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.text