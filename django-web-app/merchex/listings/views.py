# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

from listings.form import BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list (request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, band_id):
  band = Band.objects.get(id=band_id)
  return render(request,
          'listings/band_detail.html',
          {'band': band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def about (request):
    return render(request, 'listings/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request,
              'listings/contact.html',
              {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def listings (request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'listings': listings})


def listing_detail(request, listing_id):
  listing = Listing.objects.get(id=listing_id)
  return render(request,
          'listings/listings_detail.html',
          {'listing': listing})


def listing_band(request, band_id):
  band = Band.objects.get(id=band_id)
  return render(request,
          'listings/listings_band.html',
          {'band': band})
