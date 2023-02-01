from rest_framework import serializers

class CookieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

class BakedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cookie_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    size = serializers.CharField(max_length=1)
    location = serializers.CharField(max_length=2)