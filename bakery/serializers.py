from rest_framework import serializers
from bakery.models import Cookie, Baked, Dough, StoreCookie

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ['id', 'name', 'mega_baked', 'mini_baked', 'dough_made', 'mega_total_in_store', 'mini_total_in_store']
        
    mega_baked = serializers.SerializerMethodField(method_name='calculate_mega_baked')
    mini_baked = serializers.SerializerMethodField(method_name='calculate_mini_baked')
    dough_made = serializers.SerializerMethodField(method_name='calculate_dough')
    mega_total_in_store = serializers.SerializerMethodField(method_name='calculate_store_mega')
    mini_total_in_store = serializers.SerializerMethodField(method_name='calculate_store_mini')
    
    def calculate_mega_baked(self, cookie:Cookie):
        baked_queryset = Baked.objects.filter(cookie=cookie)
        quantity = 0
        for baked in baked_queryset:
            if baked.size == 'L':
                quantity += baked.quantity
        return quantity
    
    def calculate_mini_baked(self, cookie:Cookie):
        baked_queryset = Baked.objects.filter(cookie=cookie)
        quantity = 0
        for baked in baked_queryset:
            if baked.size == 'S':
                quantity += baked.quantity
        return quantity
    
    def calculate_dough(self, cookie:Cookie):
        dough_queryset = Dough.objects.filter(cookie=cookie)
        quantity = 0
        for dough in dough_queryset:
            quantity += dough.quantity
        return quantity
    
    def calculate_store_mega(self, cookie:Cookie):
        store_queryset = StoreCookie.objects.filter(cookie=cookie)
        quantity = 0
        for mega in store_queryset:
            if mega.size == 'L':
                quantity += mega.quantity
        return quantity
    
    def calculate_store_mini(self, cookie:Cookie):
        store_queryset = StoreCookie.objects.filter(cookie=cookie)
        quantity = 0
        for mini in store_queryset:
            if mini.size == 'S':
                quantity += mini.quantity
        return quantity
    

class BakedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baked
        fields = ['id', 'cookie', 'cookie_name', 'quantity', 'size', 'status', 'location', 'date_baked']
        
    cookie_name = serializers.StringRelatedField(read_only=True, source='cookie')

class DoughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dough
        fields = ['id', 'cookie', 'cookie_name', 'quantity', 'location', 'date_frozen']
        
    cookie_name = serializers.StringRelatedField(read_only=True, source='cookie')
    
class StoreCookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCookie
        fields = ['id', 'cookie', 'cookie_name', 'quantity', 'size', 'last_updated']
        
    cookie_name = serializers.StringRelatedField(read_only=True, source='cookie')
