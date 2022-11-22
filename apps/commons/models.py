from django.db import models

# Create your models here.


class NameDescModel(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True)

    class Meta:
        abstract = True
