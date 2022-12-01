from apps.commons.serializers import DynamicFieldsModelSerializer

from rest_framework import serializers

from ....models import Contact, Service, Client


class ContactSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message']


class ServiceSerializer(DynamicFieldsModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Service
        fields = ['uuid', 'name', 'desc', 'image']


class ClientSerializer(DynamicFieldsModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Client
        fields = ['uuid', 'name', 'desc', 'web_url', 'client_type', 'image']
