"""
Mapemando as URLs dos Imóveis
"""

from django.urls import path, include

from rest_framework import routers

from .views import (
    PropertiesViewSet,
    AdvertisementViewSet,
)


router = routers.DefaultRouter()
router.register(r'properties', PropertiesViewSet)
router.register(r'advertisement', AdvertisementViewSet)


app_name = 'properties'

urlpatterns = [
    path('', include(router.urls)),
]
