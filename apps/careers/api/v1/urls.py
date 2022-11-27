from django.urls import path
from rest_framework import routers

from .views.careers import CareerViewSet, DropCVViewSet
ROUTER = routers.DefaultRouter()

ROUTER.register('', CareerViewSet, basename='career-viewset')
# ROUTER.register('apply', ApplicantViewSet, basename='applicant-viewset')
ROUTER.register('drop-your-cv', DropCVViewSet, basename='cv-viewset')

urlpatterns = ROUTER.urls
