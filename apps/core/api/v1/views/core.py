import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.commons.mixins.viewsets import ListCreateRetrieveViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin
from apps.core.models import Contact, Service, Client
from ..serializer.core import ContactSerializer, ServiceSerializer, ClientSerializer

from config.settings.env import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL


class ContactViewSet(ListCreateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ServiceViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'


class ClientViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'

