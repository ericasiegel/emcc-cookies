from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

# Create your views here.
class CookieViewSet(ModelViewSet):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if Dough.objects.filter(cookie_id=kwargs['pk']).count() or Baked.objects.filter(cookie_id=kwargs['pk']).count() or StoreCookie.objects.filter(cookie_id=kwargs['pk']).count():
            return Response({'error': 'Cookie can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
    # def destroy(self, request, pk):
    #     cookie = get_object_or_404(Cookie, pk=pk)
    #     if cookie.dough_set.exists() or cookie.baked_set.exists() or cookie.storecookie_set.exists():
    #         return Response({'error': 'Cookie can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     cookie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class BakedViewSet(ModelViewSet):
    queryset = Baked.objects.select_related('cookie').all()
    serializer_class = BakedSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}

class DoughViewSet(ModelViewSet):
    queryset = Dough.objects.select_related('cookie').all()
    serializer_class = DoughSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}

class StoreViewSet(ModelViewSet):
    queryset = StoreCookie.objects.select_related('cookie').all()
    serializer_class = StoreCookieSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
