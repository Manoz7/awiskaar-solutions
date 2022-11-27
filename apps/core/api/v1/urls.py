from django.urls import path
from rest_framework import routers

from .views.core import ContactViewSet, ServiceViewSet,ClientViewSet

ROUTER = routers.DefaultRouter()

ROUTER.register('contact', ContactViewSet, basename='contact-viewset')
ROUTER.register('service', ServiceViewSet, basename='service-viewset')
ROUTER.register('client', ClientViewSet, basename='client-viewset')

urlpatterns = ROUTER.urls

