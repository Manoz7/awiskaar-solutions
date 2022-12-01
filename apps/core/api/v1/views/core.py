import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from apps.commons.mixins.viewsets import ListCreateRetrieveDestroyViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, \
    DestroyViewSetMixin
from apps.core.models import Contact, Service, Client
from ..serializer.core import ContactSerializer, ServiceSerializer, ClientSerializer
from ....utils import send_contact_request_mail


class ContactViewSet(ListCreateRetrieveDestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    # Connect form to gmail
    # @action(methods=['post'], url_path='add', url_name='add', detail=False)
    # def contact_request(self, request, *args, **kwargs):
    #     ser = self.get_serializer(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     contact = Contact.objects.create(**ser.validated_data)
    #     contact.save()
    #     send_contact_request_mail(contact.id)
    #
    #     return Response(
    #         {"details": "Contact Request Successful"}
    #     )


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
