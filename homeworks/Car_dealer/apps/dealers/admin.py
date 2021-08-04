from django.contrib import admin
from apps.dealers.models import Dealer, City, Country


class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', )
    autocomplete_fields = ('city', )
    search_fields = ('title', )


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )
    autocomplete_fields = ('country', )
    search_fields = ('name', )


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )
    search_fields = ('name', )


admin.site.register(Dealer, DealerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
