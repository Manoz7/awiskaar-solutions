from django.db import models
import uuid
# Create your models here.


class NameDescModel(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True)

    class Meta:
        abstract = True


class BaseUUIDModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    class Meta:
        abstract = True
