from django.conf.urls import url

from .views import HomePageView, search, LocationCreateView, FavouritePhotoListView, toggle_favourite_photo

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^search/$', search, name='search'),
    url(r'^location/add/$', LocationCreateView.as_view(), name='create-location'),
    url(r'^favourites/$', FavouritePhotoListView.as_view(), name='favourites'),
    url(r'^toggle-favourite/$', toggle_favourite_photo, name='toggle-favourite'),
]
