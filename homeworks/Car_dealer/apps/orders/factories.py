import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Mikhail'
    last_name = 'Chabanenko'
    email = 'test@gmail.com'
    phone = '+380684635829'
    car_id = 1