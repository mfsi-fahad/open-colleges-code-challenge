from django.views.generic import FormView

from .forms import SearchForm


class HomePageView(FormView):
    template_name = 'flickr/home.html'
    form_class = SearchForm
