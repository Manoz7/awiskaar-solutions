from django.contrib import admin
from .models import CareerInfoModel, CVCareerModel, CareerApplyModel
# Register your models here.

admin.site.register([CareerApplyModel, CareerInfoModel, CVCareerModel])
