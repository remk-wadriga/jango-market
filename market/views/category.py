from django.http import HttpResponse


def products_list(request, id):
    return HttpResponse('Product of category list page. Category ID is %s' % id)
