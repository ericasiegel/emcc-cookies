from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('EPIC COOKIES!!')

@api_view()
def cookie_list(request):
    return Response('ok')

@api_view()
def cookie_detail(request, id):
    return Response(id)