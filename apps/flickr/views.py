from django.views.generic import FormView, CreateView, ListView
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import SearchForm, LocationForm
from .models import Location, FavouritePhoto
from .utils import flickr_search_by_lat_long, generate_flickr_thumbnail_url_from_search_result


class HomePageView(FormView):
    """
    View for home page
    """
    template_name = 'flickr/home.html'
    form_class = SearchForm


@require_http_methods(['POST', ])
def search(request):
    """
    View for searching photos
    """
    search_type = request.POST.get('search_type', 'name')
    page_number = request.POST.get('page_number', 1)

    if search_type == 'name':
        location_id = request.POST.get('location_id', None)

        if location_id:
            location = get_object_or_404(Location, pk=location_id)
            latitude = location.latitude
            longitude = location.longitude

    else:
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)

    search_response = flickr_search_by_lat_long(
        lat=latitude, lon=longitude, page_number=page_number
    )
    photos = search_response['photos']['photo']

    photos_with_thumbnail = list()

    for photo in photos:
        # check if photo is in favourite list
        is_favourite = FavouritePhoto.check_favourite(
            uid=photo['id'], farm=photo['farm'], server=photo['server'], secret=photo['secret'], title=photo['title']
        )

        photos_with_thumbnail.append({
            'uid': photo['id'],
            'farm': photo['farm'],
            'server': photo['server'],
            'secret': photo['secret'],
            'title': photo['title'],
            'is_favourite': is_favourite,
            'thumbnail_url': generate_flickr_thumbnail_url_from_search_result(photo)
        })

    return JsonResponse(photos_with_thumbnail, safe=False)


class LocationCreateView(SuccessMessageMixin, CreateView):
    """
    View for adding locations
    """
    form_class = LocationForm
    template_name = 'flickr/create-location.html'
    success_url = reverse_lazy('create-location')
    success_message = '%(name)s added successfully'


class FavouritePhotoListView(ListView):
    """
    View for listing favourite photos
    """
    queryset = FavouritePhoto.objects.all()
    template_name = 'flickr/favourites.html'
    context_object_name = 'favourite_photos'


@require_http_methods(['POST', ])
def toggle_favourite_photo(request):
    """
    View for toggling a photo as favourite
    """
    uid = request.POST.get('uid', None)
    farm = request.POST.get('farm', None)
    server = request.POST.get('server', None)
    secret = request.POST.get('secret', None)
    title = request.POST.get('title', None)

    if uid and farm and server and secret and title:
        # check if it is already in favourites
        favourite_photo = FavouritePhoto.objects.filter(
            uid=uid, farm=farm, server=server, secret=secret, title=title
        ).first()

        if favourite_photo:
            favourite_photo.delete()
            is_favourite = False
        else:
            # adding favourite
            FavouritePhoto.objects.create(
                uid=uid, farm=farm, server=server, secret=secret, title=title
            )
            is_favourite = True

        response_data = {
            'is_favourite': is_favourite
        }
    else:
        response_data = {
            'message': 'Something went wrong.'
        }

    return JsonResponse(response_data)
