from django.test import TestCase

from apps.cars.tests.factories import CarFactory
from apps.orders.models import Order


class TestOrderModel(TestCase):
    def setUp(self) -> None:
        self.car = CarFactory()

    def test_model(self):
        order = Order.objects.create(
            first_name='Mikhail',
            last_name='Chabanenko',
            email='test@gmail.com',
            phone='+380684635829',
            message='some text message',
            car=self.car,
        )

        self.assertIsNotNone(order.id)
        self.assertEqual(str(order), 'Mikhail Chabanenko')
        self.assertEqual(order.email, 'test@gmail.com')
        self.assertEqual(order.phone, '+380684635829')
        self.assertEqual(order.message, 'some text message')