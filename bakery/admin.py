from django.contrib import admin
from django.db.models import Sum, F, When, Q, Value, Case, IntegerField
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models



@admin.register(models.Cookie)
class CookieAdmin(admin.ModelAdmin):
    list_display = ['name', 'dough_par', 'dough_quantity', 'baked_cookie_par', 'baked_quantity', 'mini_cookie_par', 'mini_quantity', 'store_quantity']
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
            reverse('admin:bakery_baked_changelist')
            + '?'
            + urlencode({
                'cookie__id':str(cookie.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, cookie.mini_quantity)
    
    def store_quantity(self, cookie):
        return cookie.store_quantity

    def get_queryset(self, request):
        queryset = super().get_queryset(request).prefetch_related(
        'baked_set', 'dough_set', 'storecookie_set'
        )  

        return queryset.only('id').annotate(
            baked_quantity=Sum(
                Case(
                    When(Q(baked__size='L') | Q(name='cookie_name'), then=F('baked__quantity')),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            mini_quantity=Sum(
                Case(
                    When(Q(baked__size='S') | Q(name='cookie_name'), then=F('baked__quantity')),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            dough_quantity=Sum('dough__quantity'),
            store_quantity=Sum('storecookie__quantity')
        )



@admin.register(models.Baked)
class BakedAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'size', 'quantity', 'date_baked', 'status', 'location']
    list_select_related = ['cookie']
    search_fields = ['cookie_name__icontains', 'size__icontains', 'location__icontains', 'status__icontains']
    list_filter = ['size','status', 'location', 'date_baked']
    
    def cookie_name(self, baked):
        return baked.cookie.name

# @admin.register(models.Mini)
# class MiniAdmin(admin.ModelAdmin):
#     list_display = ['cookie_name', 'quantity', 'date_baked', 'status', 'location']
#     list_select_related = ['cookie']
#     search_fields = ['cookie_name__icontains', 'location__icontains', 'status__icontains']
#     list_filter = ['status', 'location', 'date_baked']
    
#     def cookie_name(self, baked):
#         return baked.cookie.name
    
@admin.register(models.Dough)
class DoughAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'quantity', 'date_frozen', 'location']
    list_select_related = ['cookie']
    search_fields = ['cookie__name__icontains', 'location__icontains']
    list_filter = ['location', 'date_frozen']
    
    def cookie_name(self, dough):
        return dough.cookie.name

@admin.register(models.StoreCookie)
class StoreCookieAdmin(admin.ModelAdmin):
    list_display = ['cookie_name', 'size', 'par', 'quantity', 'last_updated']
    list_select_related = ['cookie']
    search_fields = ['cookie__name__icontains', 'size__icontains']
    list_filter = ['size']
    
    def cookie_name(self, baked):
        return baked.cookie.name
    
# Register your models here.