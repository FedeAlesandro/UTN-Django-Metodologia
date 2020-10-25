import datetime
import uuid

from django.http import HttpResponseRedirect, Http404
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


def estate_filter(request):
    today = datetime.date.today()
    today_date = datetime.datetime.strptime(today.__str__(), "%Y-%m-%d").__str__()
    return render(request, 'rentals/filter.html', {"today_date": today_date})


def make_filter(request):
    # limpiamos las variables globales
    global estates
    global date_list
    if len(estates) != 0:
        estates = []
    if len(date_list) != 0:
        date_list = []

    if request.method == 'POST':
        since_date = request.POST['since_date']
        to_date = request.POST['to_date']
        since_date = datetime.datetime.strptime(since_date, "%Y-%m-%d").date()
        to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").date()
        date_is_valid = check_date(since_date, to_date)
        if date_is_valid:
            city = request.POST['city']
            city = city.lower()
            total_pax = request.POST['pax']
            # creamos un array de fechas con los dias requeridos
            while since_date != to_date:
                date_list.append(since_date)
                since_date = since_date + datetime.timedelta(days=1)
            date_list.append(to_date)

            try:
                city = City.objects.get(name=city)
                estates_c = Estate.objects.filter(city=city, pax=total_pax)  # filtro por ciudad y por pax

                for estate in estates_c:  # recorro todas las propiedades que cumplen con la cuidad y el pax
                    flag = 0
                    for date in date_list:  # para cada propiedad me traigo el rental_date correspondiente a esa fecha
                        rentals_date = RentalDate.objects.filter(estate_id=estate.id, date=date, reservation=None)
                        if not rentals_date:  # si rentals_date viene vacio, la propiedad no tiene ese dia para reservar
                            flag = 1
                    if flag == 0:  # si el flag es 0 significa que cumple con todas las fechas
                        estates.append(estate)
                return HttpResponseRedirect(reverse('rentals:home'))
            except City.DoesNotExist:
                return HttpResponseRedirect(reverse('rentals:home'))
        else:
            return render(request, 'rentals/filter.html', {"flag": True})


def check_date(since_date, to_date):
    if since_date > to_date:
        return False
    return True


def details(request, estate_id):
    try:
        estate = Estate.objects.get(pk=estate_id)
        subtotal = estate.amount * len(date_list)
        commission = estate.commission
        total = subtotal + subtotal*commission
        context = {
            'estate': estate,
            'since_date': date_list[0],
            'to_date': date_list[-1],
            'subtotal': subtotal,
            'commission': commission,
            'total': total,
        }
    except Estate.DoesNotExist:
        pass
    return render(request, 'rentals/details.html', context)


def reserve(request, estate_id):
    try:
        estate = get_object_or_404(Estate, pk=estate_id)
        date = datetime.date.today().__str__()
        code = uuid.uuid4().__str__()
        if request.method == 'POST':
            guest_name = request.POST['name']
            guest_last_name = request.POST['last_name']
            guest_email = request.POST['email']
            reservation = Reservation(estate=estate, date=date, code=code, guest_name=guest_name,
                                      guest_last_name=guest_last_name, guest_email=guest_email)
            reservation.save()

            for date in date_list:
                rental_date = RentalDate.objects.filter(date=date, estate=estate_id)
                rental_date = rental_date[0]
                rental_date.reservation = reservation
                rental_date.save()

            estates.remove(estate)
            amount = reservation.estate.amount * reservation.estate.rentaldate_set.filter(
                reservation=reservation).count()
            reservation.amount = amount + amount * estate.commission
            reservation.save()

            return HttpResponseRedirect(reverse('rentals:home'))
    except Estate.DoesNotExist:
        raise Http404("Ups! There was a problem!")
