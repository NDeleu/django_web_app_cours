from django import forms
from listings.models import Band, Goodies


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__'
        exclude = ('active', 'official_homepage')


class GoodiesForm(forms.ModelForm):
    class Meta:
        model = Goodies
        fields = '__all__'
