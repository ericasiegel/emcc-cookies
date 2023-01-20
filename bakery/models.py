from django.db import models

# Create your models here.
class Cookie(models.Model):
    name = models.CharField(max_length=255)

class Dough(models.Model):
    frozen_ct = models.IntegerField()
    location = models.CharField(max_length=255)
    date_frozen = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    
class Baked(models.Model):
    frozen_ct = models.IntegerField()
    location = models.CharField(max_length=255)
    date_baked = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)

# class Store(models.Model):
#     updated_at = models.DateTimeField(auto_now_add=True)
    
class StoreCookie(models.Model):
    quantity = models.IntegerField()
    cookie = models.ForeignKey(Cookie, on_delete=models.PROTECT, related_name='CookieInStore')
    

    