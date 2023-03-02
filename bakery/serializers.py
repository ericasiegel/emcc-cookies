from rest_framework import serializers
from bakery.models import *


class DisplayChoiceField(serializers.ChoiceField):
    def __init__(self, choices, **kwargs):
        super().__init__(choices, **kwargs)
        self.choice_strings_to_values = {
            key: key for key, value in self.choices.items()
        }

    def to_representation(self, value):
        return self.choices.get(value, value)

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

class CookieNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = ['id', 'name']

class BakedSerializer(serializers.ModelSerializer):
    cookie = CookieNameSerializer(read_only=True)
    cookie_id = serializers.PrimaryKeyRelatedField(queryset=Cookie.objects.all(), write_only=True, source='cookie')
    
    size = DisplayChoiceField(choices=TYPE_CHOICES)
    status = DisplayChoiceField(choices=BAKED_CHOICES)
    location = DisplayChoiceField(choices=LOCATION_CHOICES)

    
    class Meta:
        model = Baked
        fields = ['id', 'cookie','cookie_id', 'quantity', 'size', 'status', 'location', 'date_baked']



class DoughSerializer(serializers.ModelSerializer):
    cookie = CookieNameSerializer(read_only=True)
    cookie_id = serializers.PrimaryKeyRelatedField(queryset=Cookie.objects.all(), write_only=True, source='cookie')
    
    location = DisplayChoiceField(choices=LOCATION_CHOICES) 
    
    class Meta:
        model = Dough
        fields = ['id', 'cookie', 'cookie_id', 'quantity', 'location', 'date_frozen']
        

    
class StoreCookieSerializer(serializers.ModelSerializer):
    cookie = CookieNameSerializer(read_only=True)
    cookie_id = serializers.PrimaryKeyRelatedField(queryset=Cookie.objects.all(), write_only=True, source='cookie')
    
    size = DisplayChoiceField(choices=TYPE_CHOICES)
    
    class Meta:
        model = StoreCookie
        fields = ['id', 'cookie', 'cookie_id', 'quantity', 'size']
        

