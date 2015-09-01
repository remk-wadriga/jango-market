from django.shortcuts import render
from django.views import generic
from market.models import Category


def index(request):
    return render(request, 'landing/index.html')


class CatalogView(generic.ListView):
    template_name = 'landing/catalog.html'
    context_object_name = 'categories_list'
    model = Category
