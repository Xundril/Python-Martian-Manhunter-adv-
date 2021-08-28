from django.contrib import admin
from apps.cars.models import Car, Picture, Color, Model, Brand, Property, FuelType


class CarAdmin(admin.ModelAdmin):
    list_display = ('slug', 'price', 'status', 'dealer', )
    autocomplete_fields = ('dealer', 'model', 'property', )
    search_fields = ('slug', )


class ModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('brand', )
    search_fields = ('name', )


class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    search_fields = ('name', )


admin.site.register(Car, CarAdmin)
admin.site.register(Picture)
admin.site.register(Color)
admin.site.register(Model, ModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(FuelType)
