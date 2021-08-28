from django.test import TestCase

from apps.dealers.tests.factories import UserFactory, CityFactory, CountryFactory
from apps.dealers.models import Dealer, City, Country


class TestDealerModel(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.city = CityFactory()

    def test_model(self):
        dealer = Dealer.objects.create(
            title='test dealer',
            e_mail='test_email@gmail.com',
            user=self.user,
            city=self.city,
        )

        self.assertIsNotNone(dealer.id)
        self.assertEqual(str(dealer), 'test dealer')
        self.assertEqual(dealer.e_mail, 'test_email@gmail.com')


class TestCityModel(TestCase):
    def setUp(self) -> None:
        self.country = CountryFactory()

    def test_model(self):
        city = City.objects.create(
            name='Berlin',
            country=self.country,
        )

        self.assertIsNotNone(city.id)
        self.assertEqual(str(city), 'Berlin')


class TestCountryModel(TestCase):
    def test_model(self):
        country = Country.objects.create(
            name='Germany',
            code='49',
        )

        self.assertIsNotNone(country.id)
        self.assertEqual(str(country), 'Germany')
        self.assertEqual(country.code, '49')
