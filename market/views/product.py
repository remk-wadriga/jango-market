from django.http import HttpResponse


def index(request, id):
    return HttpResponse('Product page. Product ID is %s' % id)
