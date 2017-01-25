from django.shortcuts import render
from django.views.generic.base import TemplateView

from random import choice

from .models import Restaurant

# Create your views here.
class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self):
        restaurants = Restaurant.objects.all()
        context = super().get_context_data()
        context['restaurant'] = choice(restaurants)
        return context