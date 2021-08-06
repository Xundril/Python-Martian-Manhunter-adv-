from django.contrib import admin
from apps.restaurants.models import Restaurant, Employee, Country, City, Menu, Dish

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Menu)
admin.site.register(Dish)