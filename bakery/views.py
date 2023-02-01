from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Baked, Cookie
from .serializers import BakedSerializer, CookieSerializer


# Create your views here.
@api_view()
def cookie_list(request):
    queryset = Cookie.objects.all()
    serializer = CookieSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def baked_list(request):
    queryset = Baked.objects.all()
    serializer = BakedSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def baked_detail(request, id):
    baked = get_object_or_404(Baked, pk=id)
    serializer = BakedSerializer(baked)
    return Response(serializer.data)