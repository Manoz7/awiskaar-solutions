from django.contrib import admin
from .models import Career, Applicant, DropCVModel
# Register your models here.

admin.site.register([Career, Applicant, DropCVModel])
