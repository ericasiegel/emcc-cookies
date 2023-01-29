from django.contrib import admin
from django.db.models import Count, Sum, F
from . import models



@admin.register(models.Cookie)
class CookieAdmin(admin.ModelAdmin):
    list_display = ['name', 'baked_quantity', 'dough_quantity', 'store_quantity']
    title = 'Cookie Name'
    
    def baked_quantity(self, cookie):
        return cookie.baked_quantity
    
    def dough_quantity(self, cookie):
        return cookie.dough_quantity
    
    def store_quantity(self, cookie):
        return cookie.store_quantity
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            baked_quantity = Sum('baked__quantity'),
            dough_quantity = Sum('dough__quantity'),
            store_quantity = F('storecookie__quantity')
        )

        
        

@admin.register(models.Baked)
class BakedAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_baked', 'status', 'location']
    list_select_related = ['cookie']
    
    def cookie_name(self, baked):
        return baked.cookie.name
    
@admin.register(models.Dough)
class DoughAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_frozen', 'location']
    list_select_related = ['cookie']
    
    def cookie_name(self, dough):
        return dough.cookie.name

@admin.register(models.StoreCookie)
class StoreCookieAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'last_updated']
    list_select_related = ['cookie']
    
    def cookie_name(self, baked):
        return baked.cookie.name
    
# Register your models here.