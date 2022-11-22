from django.db import models
from apps.commons.models import NameDescModel


# Create your models here.
class DemoModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()


# Services Model
class Service(NameDescModel):
    ser_image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


# Partners Model
class Partner(NameDescModel):
    part_image = models.ImageField(upload_to='partners/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


# Clients Model
class Client(NameDescModel):
    web_url = models.URLField(max_length=50)
    client_image = models.ImageField(upload_to='clients/', null=True, blank=True)
    client_type = models.CharField(max_length=50, blank=True,
                                   help_text="signifies if the client type is personal, college, business, school.....")

    def __str__(self):
        return f"{self.name} : {self.web_url}"

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} : {self.subject}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
