import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse

from apps.commons.mixins.viewsets import ListCreateRetrieveViewSetMixin
from apps.core.models import Contact, Service, Partner, Client
from ..serializer.core import ContactSerializer, ServiceSerializer


class ContactViewSet(ListCreateRetrieveViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ServiceViewSet(ListCreateRetrieveViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

