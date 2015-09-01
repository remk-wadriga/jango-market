from django.views import generic
from market.models import Product


class IndexView(generic.DetailView):
    model = Product
    template_name = 'product/index.html'
