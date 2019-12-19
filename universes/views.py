from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from universes.models import Universe
from universes.forms import UniverseCreateForm

class UniverseListView(ListView):
    model = Universe

    def get(self, request):
        universes = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'universes/universe_list.html', {
            'universe': universes
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