from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True)
    luxury = models.BooleanField(default=False, null=True, blank=False )
    luxury = models.BooleanField(default=False, null=True, blank=False )
    luxury_1 = models.BooleanField(default=False, null=True, blank=False )
    luxury_2 = models.BooleanField(default=False, null=True, blank=False )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url