from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.models import Band, Goodies
from listings.forms import BandForm, GoodiesForm, ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    goodies = Goodies.objects.all()
    return render(request, 'listings/listings.html', {'goodies': goodies})


def goody_detail(request, goody_id):
    goody = Goodies.objects.get(id=goody_id)
    return render(request, 'listings/goody_detail.html', {'goody': goody})


def goody_create(request):
    if request.method == 'POST':
        form = GoodiesForm(request.POST)
        if form.is_valid():
            goody = form.save()
            return redirect('goody-detail', goody.id)
    else:
        form = GoodiesForm()

    return render(request, 'listings/goody_create.html', {'form': form})


def goody_update(request, goody_id):
    goody = Goodies.objects.get(id=goody_id)

    if request.method == 'POST':
        form = GoodiesForm(request.POST, instance=goody)
        if form.is_valid():
            form.save()
            return redirect('goody-detail', goody.id)
    else:
        form = GoodiesForm(instance=goody)

    return render(request, 'listings/goody_update.html', {'form': form})


def goody_delete(request, goody_id):
    goody = Goodies.objects.get(id=goody_id)

    if request.method == 'POST':
        goody.delete()
        return redirect('goody-list')

    return render(request, 'listings/goody_delete.html', {'goody': goody})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def contact(request):
    # l envoie d un vrai mail se ferai grace
    # a la configuration d un serveur SMTP

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f"Message from "
                              f"{form.cleaned_data['name'] or 'anonyme'} "
                              f"via MerchEx Contact Us form",
                      message=form.cleaned_data["message"],
                      from_email=form.cleaned_data["email"],
                      recipient_list=["admin@merchex.xyz"]
                      )
            return redirect('email-sent')

    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})
