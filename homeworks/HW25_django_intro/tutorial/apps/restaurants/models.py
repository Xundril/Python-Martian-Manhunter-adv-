from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AUTH_USER_MODEL = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    personal = models.ManyToManyField(
        'restaurants.Employee'
    )
    country = models.OneToOneField(
        'restaurants.Country',
        on_delete=models.SET_NULL,
        null=True,
    )
    city = models.OneToOneField(
        'restaurants.City',
        on_delete=models.SET_NULL,
        null=True,
    )
    menu = models.ManyToManyField(
        'restaurants.Menu'
    )

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'


class Employee(models.Model):
    POSITION_MANAGER = 'manager'
    POSITION_WAITER = 'waiter'
    POSITION_CLEANER = 'cleaner'
    POSITION_COOK = 'cook'

    POSITION_CHOICES = (
        (POSITION_MANAGER, "Manager"),
        (POSITION_WAITER, "Waiter"),
        (POSITION_CLEANER, "Cleaner"),
        (POSITION_COOK, "Cook"),
    )

    name = models.CharField(max_length=80)
    position = models.CharField(
        max_length=16,
        choices=POSITION_CHOICES,
        blank=True,
    )

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Country(models.Model):
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class City(models.Model):
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'


class Menu(models.Model):
    SEASON_SPRING = 'spring'
    SEASON_SUMMER = 'summer'
    SEASON_FALL = 'autumn'
    SEASON_WINTER = 'winter'

    SEASON_CHOICES = (
        (SEASON_SPRING, "Spring Menu"),
        (SEASON_SUMMER, "Summer Menu"),
        (SEASON_FALL, "Autumn Menu"),
        (SEASON_WINTER, "Winter Menu"),
    )

    season = models.CharField(
        max_length=20,
        choices=SEASON_CHOICES,
        default=SEASON_SPRING,
        blank=True,
    )
    name = models.CharField(max_length=80)
    dish = models.ManyToManyField(
        'restaurants.Dish'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class Dish(models.Model):
    dish = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
