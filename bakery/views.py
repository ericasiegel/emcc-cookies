from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .models import *
from .serializers import *

# Create your views here.
class CookieList(ListCreateAPIView):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

class CookieDetail(APIView):
    def get(self, request, id):
        cookie = get_object_or_404(Cookie, pk=id)
        serializer = CookieSerializer(cookie)
        return Response(serializer.data)
    def put(self, request, id):
        cookie = get_object_or_404(Cookie, pk=id)
        serializer = CookieSerializer(cookie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        cookie = get_object_or_404(Cookie, pk=id)
        doughs = cookie.dough_set.all()
        bakeds = cookie.baked_set.all()
        store_cookies = cookie.storecookie_set.all()
        if any(dough.quantity > 0 for dough in doughs) or any(baked.quantity > 0 for baked in bakeds) or any(store_cookie.quantity > 0 for store_cookie in store_cookies):
            return Response({'error': 'Cookie can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        cookie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BakedList(ListCreateAPIView):
    queryset = Baked.objects.select_related('cookie').all()
    serializer_class = BakedSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    

class BakedDetail(APIView):
    def get(self, request, id):
        baked = get_object_or_404(Baked, pk=id)
        serializer = BakedSerializer(baked)
        return Response(serializer.data)
    def put(self, request, id):
        baked = get_object_or_404(Baked, pk=id)
        serializer = BakedSerializer(baked, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        baked = get_object_or_404(Baked, pk=id)
        baked.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class DoughList(ListCreateAPIView):
    queryset = Dough.objects.select_related('cookie').all()
    serializer_class = DoughSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}


class DoughDetail(APIView):
    def get(self, request, id):
        dough = get_object_or_404(Dough, pk=id)
        serializer = DoughSerializer(dough)
        return Response(serializer.data)
    def put(self, request, id):
        dough = get_object_or_404(Dough, pk=id)
        serializer = DoughSerializer(dough, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        dough = get_object_or_404(Dough, pk=id)
        dough.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class StoreCookieList(ListCreateAPIView):
    queryset = StoreCookie.objects.select_related('cookie').all()
    serializer_class = StoreCookieSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    

class StoreCookieDetail(APIView):
    def get(self, request, id):
        storecookie = get_object_or_404(StoreCookie, pk=id)
        serializer = StoreCookieSerializer(storecookie)
        return Response(serializer.data)
    def put(self, request, id):
        storecookie = get_object_or_404(StoreCookie, pk=id)
        serializer = StoreCookieSerializer(storecookie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        storecookie = get_object_or_404(StoreCookie, pk=id)
        storecookie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
