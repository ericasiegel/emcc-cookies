from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cookies/', views.cookie_list),
    path('cookies/<int:id>/', views.cookie_detail)
]