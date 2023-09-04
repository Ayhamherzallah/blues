from django.contrib import admin
from . import models
# Register your models here.


class display(admin.ModelAdmin):
    list_display = ('id', 'product', 'size', 'Flavor', 'price')


class CatDisplay(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(models.Category, CatDisplay)
admin.site.register(models.SubCategory, CatDisplay)
admin.site.register(models.product, CatDisplay)
admin.site.register(models.ProductVariant, display)
admin.site.register(models.MenuItems, CatDisplay)

