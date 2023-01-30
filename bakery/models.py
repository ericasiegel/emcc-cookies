from django.db import models


TOP_FREEZER = 'T'
BOTTOM_FREEZER = 'B'
REFRIGERATOR = 'R'
STORAGE_FREEZER = 'SF'
STORAGE_REFRIGERATOR = 'SR'

    
LOCATION_CHOICES = [
    (TOP_FREEZER, 'Top Freezer'),
    (BOTTOM_FREEZER, 'Bottom Freezer'),
    (REFRIGERATOR, 'Refrigerator'),
    (STORAGE_FREEZER, 'Storage Freezer'),
    (STORAGE_REFRIGERATOR, 'Storage Refrigerator')
]

PACKAGED = 'P'
FROZEN = 'F'
    
BAKED_CHOICES = [
    (PACKAGED, 'Packaged'),
    (FROZEN, 'Frozen')
]

# Create your models here.
class Cookie(models.Model):
    name = models.CharField(max_length=255)
    baked_cookie_par = models.IntegerField(null=True)
    dough_par = models.IntegerField(null=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name
        
        

class Dough(models.Model):
    quantity = models.IntegerField()
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=TOP_FREEZER)
    date_frozen = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Cookie Dough'
    
class Baked(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=BAKED_CHOICES, default=FROZEN)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=TOP_FREEZER)
    date_baked = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Baked Cookie'

class Mini(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=BAKED_CHOICES, default=FROZEN)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=TOP_FREEZER)
    date_baked = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Mini Cookie'

class StoreCookie(models.Model):
    quantity = models.IntegerField()
    par = models.IntegerField(null=True)
    cookie = models.OneToOneField(Cookie, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Cookies In Store'
    
    

    