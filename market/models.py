from django.db import models
from market.ext.File import Storage
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.IntegerField(default=0)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.ForeignKey(Country)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' (' + self.country.name + ')'


class Property(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True)
    cost_coefficient = models.FloatField()

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    TYPE_DISABLED = 0
    TYPE_ENABLED = 1
    TYPE_DELETED = 2
    TYPES = [(TYPE_DISABLED, 'Неактивен'), (TYPE_ENABLED, 'Активен'), (TYPE_DELETED, 'Удалён')]

    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor)
    categories = models.ManyToManyField(Category)
    cost = models.FloatField()
    rate = models.IntegerField(blank=True, default=0)
    count = models.FloatField(blank=True, default=0)
    unit = models.ForeignKey(Unit)
    min_count = models.FloatField(blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=TYPES)
    date_added = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def default_image():
        return settings.STATIC_URL + 'img/no_image.png'

    @staticmethod
    def default_miniature():
        return settings.STATIC_URL + 'img/no_image_miniature.png'

    def primary_image(self):
        try:
            primary_size = ImageSize.objects.get(type=ImageSize.TYPE_PRIMARY)
            img = self.image_set.get(size_id=primary_size.id)
        except ObjectDoesNotExist:
            img = self.default_image()

        return img

    def miniature_image(self):
        try:
            miniature_size = ImageSize.objects.get(type=ImageSize.TYPE_MINIATURE)
            img = self.image_set.get(size_id=miniature_size.id)
        except ObjectDoesNotExist:
            img = self.default_miniature()

        return img


class ProductProperty(models.Model):
    product = models.ForeignKey(Product)
    property = models.ForeignKey(Property)
    value = models.CharField(max_length=255)


class ImageSize(models.Model):
    TYPE_MINIATURE = 0
    TYPE_PRIMARY = 1
    TYPE_SIZE = 2
    TYPES = [(TYPE_MINIATURE, 'Миниатюра'), (TYPE_PRIMARY, 'Основное изображение'), (TYPE_SIZE, 'Обычное изображение')]

    type = models.IntegerField(default=TYPE_SIZE, choices=TYPES)
    width = models.IntegerField()
    height = models.IntegerField()

    def name(self):
        size = str(self.width) + 'x' + str(self.height)
        if self.type == self.TYPE_SIZE:
            return size
        else:
            name = str(self.type)
            for type in self.TYPES:
                if type[0] == self.type:
                    name = type[1]
                    break

            return name + ' (' + size + ')'

    def __str__(self):
        return self.name()


class Image(models.Model):
    path = models.ImageField(upload_to='products', max_length=400, storage=Storage())
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product)
    size = models.ForeignKey(ImageSize)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.path.url

    def width(self):
        return self.size.width

    def height(self):
        return self.size.height
