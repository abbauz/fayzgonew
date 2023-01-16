from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from fayzgo.users.api.views import UserViewSet
from fayzgo.fayzgoapp.views import AboutView, PartnerView, ServiceView, ClientView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register('abouts', AboutView, basename='abouts')
router.register('partners', PartnerView, basename='partners')
router.register('services', ServiceView, basename='services')
router.register('clients', ClientView, basename='clients')

app_name = "api"
urlpatterns = router.urls
