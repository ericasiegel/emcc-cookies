from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET', 'POST'])
def cookie_list(request):
    if request.method == 'GET':
        queryset = Cookie.objects.all()
        serializer = CookieSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CookieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def cookie_detail(request, id):
    cookie = get_object_or_404(Cookie, pk=id)
    
    if request.method == 'GET':
        serializer = CookieSerializer(cookie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CookieSerializer(cookie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        doughs = cookie.dough_set.all()
        bakeds = cookie.baked_set.all()
        store_cookies = cookie.storecookie_set.all()
        if any(dough.quantity > 0 for dough in doughs) or any(baked.quantity > 0 for baked in bakeds) or any(store_cookie.quantity > 0 for store_cookie in store_cookies):
            return Response({'error': 'Cookie can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        cookie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'POST'])
def baked_list(request):
    if request.method == 'GET':
        queryset = Baked.objects.select_related('cookie').all()
        serializer = BakedSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BakedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def baked_detail(request, id):
    baked = get_object_or_404(Baked, pk=id)
    if request.method == 'GET':
        serializer = BakedSerializer(baked)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BakedSerializer(baked, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        baked.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def dough_list(request):
    if request.method == 'GET':
        queryset = Dough.objects.select_related('cookie').all()
        serializer = DoughSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DoughSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def dough_detail(request, id):
    dough = get_object_or_404(Dough, pk=id)
    if request.method == 'GET':
        serializer = DoughSerializer(baked)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DoughSerializer(dough, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        dough.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def storecookie_list(request):
    if request.method == 'GET':
        queryset = StoreCookie.objects.select_related('cookie').all()
        serializer = StoreCookieSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StoreCookieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def storecookie_detail(request, id):
    storecookie = get_object_or_404(StoreCookie, pk=id)
    if request.method == 'GET':
        serializer = StoreCookieSerializer(storecookie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StoreCookieSerializer(storecookie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        storecookie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)