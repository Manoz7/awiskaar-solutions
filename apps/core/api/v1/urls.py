from django.urls import path
from rest_framework import routers

from .views.core import ContactViewSet, ServiceViewSet,ClientViewSet

ROUTER = routers.DefaultRouter()

ROUTER.register('contact_request', ContactViewSet, basename='contact-viewset')
ROUTER.register('services', ServiceViewSet, basename='service-viewset')
ROUTER.register('clients', ClientViewSet, basename='client-viewset')

urlpatterns = ROUTER.urls

