from django.db import models


class Car(models.Model):
    ENGINE_HEAT = 'heat'
    ENGINE_HYBRID = 'hybrid'
    ENGINE_ELECTRIC = 'electric'

    ENGINE_CHOICES = (
        (ENGINE_HEAT, "Heat engine"),
        (ENGINE_HYBRID, "Hybrid engine"),
        (ENGINE_ELECTRIC, "Electric engine")
    )

    POLLUTANT_A_PLUS = 'a+'
    POLLUTANT_A = 'a'
    POLLUTANT_B = 'b'
    POLLUTANT_C = 'c'
    POLLUTANT_D = 'd'
    POLLUTANT_E = 'e'
    POLLUTANT_F = 'f'
    POLLUTANT_G = 'g'

    POLLUTANT_CHOICES = (
        (POLLUTANT_A_PLUS, "A+"),
        (POLLUTANT_A, "A"),
        (POLLUTANT_B, "B"),
        (POLLUTANT_C, "C"),
        (POLLUTANT_D, "D"),
        (POLLUTANT_E, "E"),
        (POLLUTANT_F, "F"),
        (POLLUTANT_G, "G")
    )

    STATUS_ACTIVE = 'active'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, "Active"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived")
    )

    GEAR_MANUAL = 'manual'
    GEAR_AUTOMATIC = 'automatic'
    GEAR_SEMI_AUTOMATIC = 'semi-automatic'

    GEAR_CHOICES = (
        (GEAR_MANUAL, "Manual"),
        (GEAR_AUTOMATIC, "Automatic"),
        (GEAR_SEMI_AUTOMATIC, "Semi-Automatic")
    )

    engine_type = models.CharField(
        max_length=20,
        choices=ENGINE_CHOICES,
        default=ENGINE_HEAT,
    )
    pollutant_type = models.CharField(
        max_length=10,
        choices=POLLUTANT_CHOICES,
        default=POLLUTANT_A,
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=50_000,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )
    doors = models.PositiveSmallIntegerField(
        default=4,
    )
    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=1.5,
    )
    gear_case = models.CharField(
        max_length=20,
        choices=GEAR_CHOICES,
        default=GEAR_AUTOMATIC,
    )
    number = models.CharField(
        max_length=15,
    )
    slug = models.SlugField(
        max_length=75,
    )
    sitting_place = models.PositiveSmallIntegerField(
        default=4,
    )
    first_registration_date = models.DateTimeField(
        auto_now_add=True,
    )
    engine_power = models.PositiveSmallIntegerField()

    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    picture = models.ForeignKey(
        'cars.Picture',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    property = models.ManyToManyField(
        'cars.Property',
    )
    fuel = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Picture(models.Model):
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True,
    )
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class Color(models.Model):
    name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Model(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
    )

    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
        verbose_name='models',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Brand(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Property(models.Model):
    CATEGORY_SMALL = 'small'
    CATEGORY_MIDSIZE = 'midsize'
    CATEGORY_LARGE = 'large'
    CATEGORY_LUXURY = 'luxury'
    CATEGORY_SPORTS = 'sports'

    CATEGORY_CHOICES = (
        (CATEGORY_SMALL, "Small"),
        (CATEGORY_MIDSIZE, "Midsize"),
        (CATEGORY_LARGE, "Large"),
        (CATEGORY_LUXURY, 'Luxury'),
        (CATEGORY_SPORTS, "Sports")
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_MIDSIZE,
    )
    name = models.CharField(
        max_length=80,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class FuelType(models.Model):
    FUEL_PETROL = 'petrol'
    FUEL_DIESEL = 'diesel'
    FUEL_GAS = 'gas'
    FUEL_ELECTRIC = 'electric'

    FUEL_CHOICES = (
        (FUEL_PETROL, "Petrol"),
        (FUEL_DIESEL, "Diesel"),
        (FUEL_GAS, "Gas"),
        (FUEL_ELECTRIC, "Electric")
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        default=FUEL_PETROL,
        unique=True,
    )

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = 'Fuel Type'
        verbose_name_plural = 'Fuel Types'
