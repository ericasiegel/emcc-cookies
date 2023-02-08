from django.urls import path

from . import views

urlpatterns = [
    path('cookies/', views.cookie_list),
    path('cookies/<int:id>/', views.cookie_detail),
    path('baked/', views.baked_list),
    path('baked/<int:id>/', views.baked_detail),
    path('dough/', views.dough_list),
    path('dough/<int:id>/', views.dough_detail),
    path('storecookie/', views.storecookie_list),
    path('storecookie/<int:id>/', views.storecookie_detail)
]