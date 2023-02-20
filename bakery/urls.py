from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('cookies', views.CookieViewSet)
router.register('baked-cookies', views.BakedViewSet)
router.register('cookie-doughs', views.DoughViewSet)
router.register('cookies-in-store', views.StoreViewSet)

urlpatterns = router.urls