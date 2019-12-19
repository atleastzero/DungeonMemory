from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from universes.models import Universe, Place
from universes.forms import UniverseCreateForm, PlaceCreateForm

class UniverseListView(ListView):
    model = Universe

    def get(self, request):
        universes = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'universes/universe_list.html', {
            'universe': universes
        })

class UniverseDetailView(DetailView):
    model = Universe

    def get(self, request, universe_id):
        universe = get_object_or_404(Universe, universe_id__exact=universe_id)
        return render(request, 'universes/universe_detail.html', {
            'universe': universe
        })

class UniverseCreateView(CreateView):
    model = Universe

    def get(self, request, *args, **kwargs):
        return render(request, 'universes/universe_create.html', {
            'form': UniverseCreateForm()
        })
    
    def post(self, request, *args, **kwargs):
        form = UniverseCreateForm(request.POST)
        if form.is_valid():
            universe = form.save()
            universe.save()
            return redirect("/", universe.universe_id)

class PlaceListView(ListView):
    model = Place

    def get(self, request, universe_id):
        places = self.get_queryset().all().order_by("-last_visited")
        return render(request, 'places/place_list.html', {
            'places': places
        })

class PlaceDetailView(DetailView):
    model = Place

    def get(self, request, universe_id, place_id):
        place = get_object_or_404(Place, place_id__exact=place_id)
        return render(request, 'places/place_detail.html', {
            'place': place
        })

class PlaceCreateView(CreateView):
    model = Place

    def get(self, request, *args, **kwargs):
        return render(request, 'places/place_create.html', {
            'form': PlaceCreateForm()
        })
    
    def post(self, request, *args, **kwargs):
        form = PlaceCreateForm(request.POST)
        if form.is_valid():
            place = form.save()
            place.save()
            return redirect("/", place.places_id)