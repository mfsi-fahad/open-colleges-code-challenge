from django.db import models


class TimestampModel(models.Model):
    """
    Abstract Base Model to add created_at and updated_at to other models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
