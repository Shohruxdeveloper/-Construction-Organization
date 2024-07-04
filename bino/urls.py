from django.urls import path, include
from .views import TerritoryView, OrganizationView, BuildingView

from rest_framework import routers

router = routers.SimpleRouter()
router.register('territory', TerritoryView, basename='territory')
router.register('organization', OrganizationView, basename='organization')
router.register('building', BuildingView, basename='building')


urlpatterns = [
    path('api/v1/', include(router.urls))
]
