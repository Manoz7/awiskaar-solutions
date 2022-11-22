from django.contrib import admin
from .models import Service, Client, Partner, Contact
# Register your models here.

admin.site.register([Service, Client, Partner, Contact])

