import uuid
import datetime
<<<<<<< HEAD
=======
from plistlib import UID
>>>>>>> c07d9d54e4e4d6455abefcd5ade74fe6c0709592
from datetime import date


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
    today = date.today()
    today_date = datetime.datetime.strptime(today.__str__(), "%Y-%m-%d").__str__()
    return render(request, 'rentals/filter.html', {"today_date": today_date})


def make_filter(request):
    try:
<<<<<<< HEAD
        # limpiamos las variables globales
=======
        #limpiamos las variables globales
>>>>>>> c07d9d54e4e4d6455abefcd5ade74fe6c0709592
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
<<<<<<< HEAD
            date_is_valid = check_date(since_date, to_date)
=======
            date_is_valid = checkDate(since_date,to_date)
>>>>>>> c07d9d54e4e4d6455abefcd5ade74fe6c0709592
            if date_is_valid:
                city = request.POST['city']
                city = city.lower()
                total_pax = request.POST['pax']
<<<<<<< HEAD
                # creamos un array de fechas con los dias requeridos
=======
                #creamos un array de fechas con los dias requeridos
>>>>>>> c07d9d54e4e4d6455abefcd5ade74fe6c0709592
                while since_date != to_date:
                    date_list.append(since_date)
                    since_date = since_date + datetime.timedelta(days=1)
                date_list.append(to_date)

                city = City.objects.get(name=city)
<<<<<<< HEAD
                estates_c = Estate.objects.filter(city=city, pax=total_pax)  # filtro por ciudad y por pax

                for estate in estates_c:  # recorro todas las propiedades que cumplen con la cuidad y el pax
                    flag = 0
                    for date in date_list:  # para cada propiedad me traigo el rental_date correspondiente a esa fecha
                        rentals_date = RentalDate.objects.filter(estate_id=estate.id, date=date)
                        if not rentals_date:  # si rentals_date viene vacio, la propiedad no tiene ese dia para reservar
                            flag = 1
                    if flag == 0:  # si el flag es 0 significa que cumple con todas las fechas
=======
                estates_c = Estate.objects.filter(city=city,pax=total_pax) #filtro por ciudad y por pax

                for estate in estates_c: #recorro todas las propiedades que cumplen con la cuidad y el pax
                    flag = 0
                    for date in date_list: #para cada propiedad me traigo el rental_date correspondiente a esa fecha
                        rentals_date = RentalDate.objects.filter(estate_id = estate.id, date=date)
                        if not rentals_date: #si rentals_date viene vacio significa que la propiedad no tiene disponible ese dia para reserva
                            flag = 1
                    if flag == 0: #si el flag es 0 significa que cumple con todas las fechas
>>>>>>> c07d9d54e4e4d6455abefcd5ade74fe6c0709592
                        estates.append(estate)
                return HttpResponseRedirect(reverse('rentals:home'))
            else:
                return render(request, 'rentals/filter.html', {"flag": True})
    except():
        raise Exception("Ups! There was a problem!")

def checkDate(since_date,to_date):
    if since_date > to_date:
        return False
    return True

def check_date(since_date, to_date):
    if since_date > to_date:
        return False
    return True


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