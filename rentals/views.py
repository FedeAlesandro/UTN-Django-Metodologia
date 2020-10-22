import uuid
import datetime
from plistlib import UID

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from rentals.models import Estate, Reservation, RentalDate, City

date_list = []
estates = []


class HomeView(generic.ListView):
    template_name = 'rentals/home.html'
    context_object_name = 'estates_list'

    def get_queryset(self):
        return estates


class DetailView(generic.DetailView):
    model = Estate
    template_name = 'rentals/details.html'


def estate_filter(request):
    return render(request, 'rentals/filter.html', None)


def make_filter(request):
    try:
        if request.method == 'POST':
            since_date = request.POST['since_date']
            to_date = request.POST['to_date']
            since_date = datetime.datetime.strptime(since_date, "%Y-%m-%d").date()
            to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
            city = request.POST['city']
            total_pax = request.POST['pax']
            while since_date != to_date:
                date_list.append(since_date)
                since_date = since_date + datetime.timedelta(days=1)
            date_list.append(to_date)
            city = City.objects.get(name=city)

            #  for date in date_list:
            #    rentals_dates = RentalDate.objects.filter(date=date)
            #    for rental_date in rentals_dates:
            #        estate = Estate.objects.get(pk=rental_date.estate_id, city=city, pax=total_pax)
            #        if not estates._contains_(estate):
            #            estates.append(estate)

            estates_aux = Estate.objects.filter(city=city, pax=total_pax)  # filtro por ciudad y por pax
            for estate in estates_aux:
                for date in date_list:
                    try:
                        rental_date = RentalDate.objects.get(estate_id=estate.id, date=date)
                        estates.append(estate)
                    except RentalDate.DoesNotExist:
                        print("xd")

            return HttpResponseRedirect(reverse('rentals:home'))
    except():
        raise Exception("Ups! There was a problem!")


def reserve(request, estate_id):
    try:
        estate = get_object_or_404(Estate, pk=estate_id)
        date = datetime.now().date()
        amount = estate.amount + (estate.amount * estate.commission)
        code = uuid.uuid4().__str__()
        if request.method == 'POST':
            guest_name = request.POST['name']
            guest_last_name = request.POST['last_name']
            guest_email = request.POST['email']
            reservation = Reservation(estate, date, code, amount,
                                      guest_name, guest_last_name, guest_email)
            reservation.save()

            for date in date_list:
                rental_date = RentalDate.objects.get(date=datetime.datetime.strptime(date, "%Y-%m-%d").date(),
                                                     estate=estate)
                rental_date.reservation = reservation
                rental_date.save()

            return HttpResponseRedirect(reverse('rentals:details', args=(estate,)))
    except():
        raise Exception("Ups! There was a problem!")
