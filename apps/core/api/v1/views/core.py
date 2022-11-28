import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.parsers import FileUploadParser

from apps.commons.mixins.viewsets import ListCreateRetrieveViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin
from apps.core.models import Contact, Service, Client
from ..serializer.core import ContactSerializer, ServiceSerializer, ClientSerializer


class ContactViewSet(ListCreateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ServiceViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    parser_classes = [FileUploadParser]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'


class ClientViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ClientSerializer
    parser_classes = [FileUploadParser]
    queryset = Client.objects.all()
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'

