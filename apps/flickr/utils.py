import os

from flickrapi import FlickrAPI, FlickrError

from . import logger
from .constants import FLICKR_THUMBNAIL_URL, FLICKR_RESULTS_PER_PAGE


def get_flickr_client():
    """
    Util function to get Flickr API client
    :return: flickr_client
    """
    flickr_client = FlickrAPI(
        api_key=os.getenv('FLICKR_API_KEY'), secret=os.getenv('FLICKR_API_SECRET'), format='parsed-json'
    )

    return flickr_client


def flickr_search_by_lat_long(lat, lon, page_number):
    """
    Util function to call Flickr Search API by latitude and longitude
    :param lat:
    :param lon:
    :return:
    """
    flickr_client = get_flickr_client()

    try:
        search_response = flickr_client.photos.search(
            lat=lat, lon=lon, per_page=FLICKR_RESULTS_PER_PAGE, page=page_number
        )

        return search_response
    except FlickrError as e:
        logger.error(e)


def generate_flickr_thumbnail_url_from_search_result(photo):
    """
    Util function to generate flickr thumbnail url of search result
    :param result:
    :return:
    """
    return FLICKR_THUMBNAIL_URL.format(
        photo['farm'], photo['server'], photo['id'], photo['secret']
    )
