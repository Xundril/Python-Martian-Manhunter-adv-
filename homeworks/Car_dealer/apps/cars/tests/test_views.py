from django.test import TestCase

from apps.cars.tests.factories import CarFactory


class CarsListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = CarFactory()
        cls.url = f'/cars/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class CarsDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.car = CarFactory()
        cls.url = f'/cars/{cls.car.slug}/'

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.number)

    def test_not_found(self):
        response = self.client.get('/cars/wrong-slug/')
        self.assertEqual(response.status_code, 404)
