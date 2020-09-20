from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView


class ComingSoonView(TemplateView):

    template_name = "csoon/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context



"""
   
def get_context_data(self, **kwargs):
    
    context = super().get_context_data(**kwargs)

    slug = self.kwargs['slug']

    # context['slug'] = self.kwargs['slug']
    
    # context['latest_games'] = Game.objects.all()[:10]
    
    game_processing_status = process_a_game(slug)
    
    context['game_processing_status'] = game_processing_status
           
    return context

"""

