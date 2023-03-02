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
        fields = ['id', 'name', 'counts']
        
    counts = serializers.SerializerMethodField(method_name='calculate_totals')
    
    def calculate_totals(self, cookie:Cookie):
        baked_queryset = Baked.objects.filter(cookie=cookie)
        dough_queryset = Dough.objects.filter(cookie=cookie)
        storecookie_queryset = StoreCookie.objects.filter(cookie=cookie)
        
        dough_total = 0
        baked_mini_quantity = 0
        baked_mega_quantity = 0
        store_mini_quantity = 0
        store_mega_quantity = 0
        
        for doughs in dough_queryset:
            dough_total += doughs.quantity

        for baked in baked_queryset:
            if baked.size == 'L':
                baked_mega_quantity += baked.quantity
            elif baked.size == 'S':
                baked_mini_quantity += baked.quantity
                
        for store in storecookie_queryset:
            if store.size == 'L':
                store_mega_quantity += store.quantity
            elif store.size == 'S':
                store_mini_quantity += store.quantity       
        
        return {
                'doughs': dough_total, 
                'baked_cookies':{'mega': baked_mega_quantity, 'mini': baked_mini_quantity}, 
                'total_in_store':{'mega': store_mega_quantity, 'mini': store_mini_quantity}
                }
    

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
        

