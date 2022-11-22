from django.urls import path
from rest_framework import routers

from .views.demo import DemoView, DemoViewSet
from .views.core import ContactViewSet, ServiceViewSet

ROUTER = routers.DefaultRouter()

ROUTER.register('demo', DemoViewSet, basename='demo-viewset')
ROUTER.register('contact', ContactViewSet, basename='contact-viewset')
ROUTER.register('service', ServiceViewSet, basename='service-viewset')

urlpatterns = ROUTER.urls

