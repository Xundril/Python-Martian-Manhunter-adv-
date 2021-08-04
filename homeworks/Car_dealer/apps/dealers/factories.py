import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'Germany'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'Berlin'
    country_id = 2


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'dealer_2'
    e_mail = 'dealer_2@mail.com'
    user_id = 2
    city_id = 2