from django.db import models

from apps.core.models import TimestampModel


class Location(TimestampModel):
    """
    Model for storing locations
    """
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    name = models.CharField(max_length=255)
