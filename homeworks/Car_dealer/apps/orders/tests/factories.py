import factory

from apps.cars.tests.factories import CarFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = factory.Sequence(lambda n: f'first_name_{n}')
    last_name = factory.Sequence(lambda n: f'last_name_{n}')
    email = factory.Sequence(lambda n: f'test_{n}@mail.com')
    phone = '+380684635829'
    car = factory.SubFactory(CarFactory)