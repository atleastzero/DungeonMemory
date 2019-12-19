from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from universes.models import Universe
from universes.forms import UniverseCreateForm

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
            return redirect("/", universe.pk)