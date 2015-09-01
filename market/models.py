from django.db import models


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
    rate = models.IntegerField(blank=True)
    count = models.FloatField()
    unit = models.ForeignKey(Unit)
    min_count = models.FloatField(blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=TYPES)
    date_added = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class ProductProperty(models.Model):
    product = models.ForeignKey(Product)
    property = models.ForeignKey(Property)
    value = models.CharField(max_length=255)


class Image(models.Model):
    path = models.ImageField(upload_to='market/media/products', max_length=400)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product)
    is_miniature = models.BooleanField()
    is_primary = models.BooleanField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
