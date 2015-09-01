from django.contrib import admin
import market.models as models


class ImageInline(admin.StackedInline):
    model = models.Image
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'vendor', 'rate', 'count')
    list_filter = ['cost', 'rate', 'count']
    search_fields = ['name']
    inlines = [ImageInline]

admin.site.register(models.Category)
admin.site.register(models.Vendor)
admin.site.register(models.Property)
admin.site.register(models.Unit)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductProperty)
admin.site.register(models.Image)
admin.site.register(models.Country)
