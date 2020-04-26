import os

from flickrapi import FlickrAPI


def get_flickr_client():
    """
    Util function to get Flickr API client
    :return: flickr_client
    """
    flickr_client = FlickrAPI(
        api_key=os.getenv('FLICKR_API_KEY'), secret=os.getenv('FLICKR_API_SECRET'), format='parsed-json'
    )

    return flickr_client
