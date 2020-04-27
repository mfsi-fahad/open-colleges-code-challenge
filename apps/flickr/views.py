from django.views.generic import FormView
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .forms import SearchForm
from .models import Location
from .utils import flickr_search_by_lat_long, generate_flickr_thumbnail_url_from_search_result


class HomePageView(FormView):
    template_name = 'flickr/home.html'
    form_class = SearchForm


@require_http_methods(['POST', ])
def search(request):
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
        photos_with_thumbnail.append({
            'title': photo['title'],
            'thumbnail_url': generate_flickr_thumbnail_url_from_search_result(photo)
        })

    return JsonResponse(photos_with_thumbnail, safe=False)
