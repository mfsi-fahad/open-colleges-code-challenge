from django.contrib import admin

from .models import Location, FavouritePhoto

admin.site.register([Location, FavouritePhoto, ])
