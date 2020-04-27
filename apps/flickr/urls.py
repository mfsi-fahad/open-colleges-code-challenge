from django.conf.urls import url

from .views import HomePageView, search

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^search/$', search, name='search'),
]
