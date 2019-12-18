from django.shortcuts import render
from django.views.generic.list import ListView

from universes.models import Universe

class UniverseListView(ListView):
    model = Universe

    def get(self, request):
        universes = self.get_queryset().all().order_by("-last_updated")
        return render(request, 'universes/universe_list.html', {
            'universe': universes
        })