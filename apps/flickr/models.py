from django.db import models

from apps.core.models import TimestampModel
from .constants import FLICKR_THUMBNAIL_URL


class Location(TimestampModel):
    """
    Model for storing locations
    """
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class FavouritePhoto(TimestampModel):
    """
    Model for storing favourite photos
    """
    uid = models.CharField(max_length=255, unique=True, verbose_name='UID')
    farm = models.IntegerField()
    server = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    title = models.CharField(max_length=2047, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.uid, self.title)

    def thumbnail_url(self):
        return FLICKR_THUMBNAIL_URL.format(
            self.farm, self.server, self.uid, self.secret
        )

    @classmethod
    def check_favourite(cls, uid, farm, server, secret, title):
        favourite_photo = cls.objects.filter(
            uid=uid, farm=farm, server=server, secret=secret, title=title
        ).first()

        if favourite_photo:
            return True
        return False

    class Meta:
        ordering = ('-created_at',)
