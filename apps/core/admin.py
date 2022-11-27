from django.contrib import admin
from .models import Service, Client, Contact
# Register your models here.

admin.site.register([Service, Client, Contact])

