import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'AA 2278 AB'
    slug = '145-MT'
    engine_power = 145
    dealer_id = 1
    picture_id = 1
    color_id = 1
    model_id = 1


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Grey'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'Audi'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'Sedan'