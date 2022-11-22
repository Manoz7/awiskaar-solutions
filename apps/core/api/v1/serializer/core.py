from apps.commons.serializers import DynamicFieldsModelSerializer

from rest_framework import serializers

from ....models import Contact, Service, Partner, Client


class ContactSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model= Contact
        fields = ['id', 'name', 'email', 'address', 'subject', 'message']


class ServiceSerializer(DynamicFieldsModelSerializer):
    ser_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'desc', 'ser_image']
