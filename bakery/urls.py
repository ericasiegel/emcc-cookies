from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('cookies', views.CookieViewSet)
router.register('baked-cookies', views.BakedViewSet, basename='baked-cookies')
router.register('cookie-doughs', views.DoughViewSet, basename='cookie-doughs')
router.register('cookies-in-store', views.StoreViewSet, basename='cookies-in-store')

urlpatterns = router.urls