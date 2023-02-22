from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cookie_id', 'size', 'location']
    search_fields = ['cookie__name']
    ordering_fields = ['date_baked', 'cookie_id', 'status', 'location']
    
    def get_serializer_context(self):
        return {'request': self.request}

class DoughViewSet(ModelViewSet):
    queryset = Dough.objects.select_related('cookie').all()
    serializer_class = DoughSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cookie_id', 'location']
    search_fields = ['cookie__name']
    ordering_fields = ['date_frozen', 'cookie_id', 'location']
    
    def get_serializer_context(self):
        return {'request': self.request}

class StoreViewSet(ModelViewSet):
    queryset = StoreCookie.objects.select_related('cookie').all()
    serializer_class = StoreCookieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cookie_id', 'size']
    search_fields = ['cookie__name']
    ordering_fields = ['cookie_id', 'size']
    
    def get_serializer_context(self):
        return {'request': self.request}
    
