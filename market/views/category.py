from django.views import generic
from market.models import Category


class ProductsView(generic.DetailView):
    model = Category
    template_name = 'category/products.html'
