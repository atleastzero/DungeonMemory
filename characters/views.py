from django.shortcuts import render
from django.views.generic.list import ListView

class CharactersSavedListView(ListView):
    model = Character

    def get(self, request):
        characters = self.get_queryset().all()
        return render(request, 'characters/character_saved_list.html')