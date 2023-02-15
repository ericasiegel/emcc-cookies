from django.urls import path

from . import views

urlpatterns = [
    path('cookies/', views.CookieList.as_view()),
    path('cookies/<int:id>/', views.CookieDetail.as_view()),
    path('baked/', views.BakedList.as_view()),
    path('baked/<int:id>/', views.BakedDetail.as_view()),
    path('dough/', views.DoughList.as_view()),
    path('dough/<int:id>/', views.DoughDetail.as_view()),
    path('storecookie/', views.StoreCookieList.as_view()),
    path('storecookie/<int:id>/', views.StoreCookieDetail.as_view())
]