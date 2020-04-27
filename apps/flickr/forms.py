from django import forms

from .models import Location


class SearchForm(forms.Form):
    locations = forms.ModelChoiceField(
        label='', queryset=Location.objects.all(), empty_label='Please select a location'
    )
    latitude = forms.DecimalField(
        label='', required=False, max_digits=10, decimal_places=7,
        widget=forms.NumberInput(attrs={'placeholder': 'Latitude'})
    )
    longitude = forms.DecimalField(
        label='', required=False, max_digits=10, decimal_places=7,
        widget=forms.NumberInput(attrs={'placeholder': 'Longitude'})
    )


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude',)
