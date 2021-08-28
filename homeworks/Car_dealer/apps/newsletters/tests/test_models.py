from django.test import TestCase

from apps.newsletters.models import NewsLetter


class TestNewsLetterModel(TestCase):
    def test_model(self):
        newsletter = NewsLetter.objects.create(
            email='newsletter_test_email@gmail.com',
        )

        self.assertIsNotNone(newsletter.id)
        self.assertEqual(str(newsletter), 'newsletter_test_email@gmail.com')