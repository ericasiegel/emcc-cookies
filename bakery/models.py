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
    PACKAGED = 'P'
    FROZEN = 'F'
    
    BAKED_CHOICES = [
        (PACKAGED, 'Packaged'),
        (FROZEN, 'Frozen')
    ]
    
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=BAKED_CHOICES, default=FROZEN)
    location = models.CharField(max_length=255)
    date_baked = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    
# class Store(models.Model):
#     last_updated = models.DateField(auto_now=False)

class StoreCookie(models.Model):
    quantity = models.IntegerField()
    cookie = models.OneToOneField(Cookie, on_delete=models.CASCADE, related_name='CookieInStore')
    last_updated = models.DateField(auto_now=True)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    

    