from django.db.models import *
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
        fields = ['id', 'name', 'dough_made', 'baked', 'total_in_store']
        
    baked = serializers.SerializerMethodField(method_name='calculate_baked')
    dough_made = serializers.SerializerMethodField(method_name='calculate_dough')
    total_in_store = serializers.SerializerMethodField(method_name='calculate_storecookie')
    
    def calculate_dough(self, cookie:Cookie):
        dough_queryset = Dough.objects.filter(cookie=cookie)
        quantity = 0
        for dough in dough_queryset:
            quantity += dough.quantity
        return quantity
    
    def calculate_baked(self, cookie:Cookie):
        baked_queryset = Baked.objects.filter(cookie=cookie)
        mini_quantity = 0
        mega_quantity = 0

        for baked in baked_queryset:
            if baked.size == 'L':
                mega_quantity += baked.quantity
            elif baked.size == 'S':
                mini_quantity += baked.quantity
        return {'mega': mega_quantity, 'mini': mini_quantity}
    
    def calculate_storecookie(self, cookie:Cookie):
        storecookie_queryset = StoreCookie.objects.filter(cookie=cookie)
        mini_quantity = 0
        mega_quantity = 0

        for scookie in storecookie_queryset:
            if scookie.size == 'L':
                mega_quantity += scookie.quantity
            elif scookie.size == 'S':
                mini_quantity += scookie.quantity
        return {'mega': mega_quantity, 'mini': mini_quantity}
    

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
        

