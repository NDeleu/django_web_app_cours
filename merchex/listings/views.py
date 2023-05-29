from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Goodies


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    goodies = Goodies.objects.all()
    return render(request, 'listings/listings.html', {'goodies': goodies})


def contact(request):
    return render(request, 'listings/contact.html')
