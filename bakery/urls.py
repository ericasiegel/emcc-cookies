from django.urls import path

from . import views

urlpatterns = [
    path('cookies/', views.cookie_list),
    path('baked/', views.baked_list),
    path('baked/<int:id>/', views.baked_detail)
]