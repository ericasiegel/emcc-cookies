from django.contrib import admin
from django.db.models import Sum, F
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models



@admin.register(models.Cookie)
class CookieAdmin(admin.ModelAdmin):
    list_display = ['name', 'baked_cookie_par', 'baked_quantity', 'mini_quantity', 'dough_par', 'dough_quantity', 'store_quantity']
    title = 'Cookie Name'
    search_fields = ['name__icontains']
    
    def baked_quantity(self, cookie):
        url = (
            reverse('admin:bakery_baked_changelist')
            + '?'
            + urlencode({
                'cookie__id':str(cookie.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, cookie.baked_quantity)
    
    def dough_quantity(self, cookie):
        url = (
            reverse('admin:bakery_dough_changelist')
            + '?'
            + urlencode({
                'cookie__id':str(cookie.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, cookie.dough_quantity)
    
    def mini_quantity(self, cookie):
        url = (
            reverse('admin:bakery_mini_changelist')
            + '?'
            + urlencode({
                'cookie__id':str(cookie.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, cookie.mini_quantity)
    
    def store_quantity(self, cookie):
        return cookie.store_quantity

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        return queryset.annotate(
            mini_quantity = Sum('mini__quantity'),
            baked_quantity = Sum('baked__quantity'),
            dough_quantity = Sum('dough__quantity'),
            store_quantity = F('storecookie__quantity')
        )


@admin.register(models.Baked)
class BakedAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_baked', 'status', 'location']
    list_select_related = ['cookie']
    search_fields = ['cookie_name__icontains', 'location__icontains', 'status__icontains']
    list_filter = ['status', 'location', 'date_baked']
    
    def cookie_name(self, baked):
        return baked.cookie.name

@admin.register(models.Mini)
class MiniAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_baked', 'status', 'location']
    list_select_related = ['cookie']
    search_fields = ['cookie_name__icontains', 'location__icontains', 'status__icontains']
    list_filter = ['status', 'location', 'date_baked']
    
    def cookie_name(self, baked):
        return baked.cookie.name
    
@admin.register(models.Dough)
class DoughAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_frozen', 'location']
    list_select_related = ['cookie']
    search_fields = ['cookie__name__icontains', 'location__icontains']
    
    def cookie_name(self, dough):
        return dough.cookie.name

@admin.register(models.StoreCookie)
class StoreCookieAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'par', 'quantity', 'last_updated']
    list_select_related = ['cookie']
    search_fields = ['cookie__name__icontains']
    
    def cookie_name(self, baked):
        return baked.cookie.name
    
# Register your models here.