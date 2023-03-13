from django.db import models
from django.core.validators import MinValueValidator

# Storage Location
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

# Baked Choices
PACKAGED = 'P'
FROZEN = 'F'
    
BAKED_CHOICES = [
    (PACKAGED, 'Packaged'),
    (FROZEN, 'Frozen')
]

# Cookie Size
MEGA = 'L'
MINI = 'S'
        
TYPE_CHOICES = [
    (MEGA, 'Mega'),
    (MINI, 'Mini')
]

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Cookie(models.Model):
    name = models.CharField(max_length=255)
    dough_par = models.PositiveSmallIntegerField(null=True)
    mega_cookie_par = models.PositiveSmallIntegerField(null=True)
    mini_cookie_par = models.PositiveSmallIntegerField(null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        
    

class Dough(models.Model):
    quantity = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=TOP_FREEZER)
    date_frozen = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Cookie Dough'

    
class Baked(models.Model):
    size = models.CharField(max_length=1, choices=TYPE_CHOICES, default=MEGA)
    quantity = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=1, choices=BAKED_CHOICES, default=FROZEN)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=TOP_FREEZER)
    date_baked = models.DateField(auto_now=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Baked Cookie'


class StoreCookie(models.Model):
    size = models.CharField(max_length=1, choices=TYPE_CHOICES, default=MEGA)
    quantity = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField(null=True)
    cookie = models.ForeignKey(Cookie, on_delete=models.PROTECT)
    last_updated = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['cookie']
        verbose_name = 'Cookies In Store'
        unique_together = [['size', 'cookie']]
        
    
    

    