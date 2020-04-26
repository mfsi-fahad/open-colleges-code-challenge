from django import forms

from .models import Location


class SearchForm(forms.Form):
    locations = forms.ModelChoiceField(queryset=Location.objects.all())
