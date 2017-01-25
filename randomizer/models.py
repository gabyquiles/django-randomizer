from django.db import models


# Create your models here.
class Restaurant(models.Model):
    """My Restaurant Model"""

    name = models.CharField(max_length=32)
