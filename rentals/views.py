from django.shortcuts import render
from django.views import generic

from rentals.models import Estate


class HomeView(generic.ListView):
    template_name = 'rentals/home.html'
    context_object_name = 'estates_list'

    def get_queryset(self):
        return Estate.objects.all()


class DetailView(generic.DetailView):
    model = Estate
    template_name = 'rentals/details.html'
