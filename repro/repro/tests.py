# In your_app/tests.py

from django.test import TestCase
from .models import TestModel
from django.utils import timezone
from psycopg2 import _range as psycopg2_range

class TestModelTestCase(TestCase):
    
    def test_range(self):
        now = timezone.now()
        empty_range = psycopg2_range.DateTimeTZRange(empty=True)

        test_model = TestModel(range=psycopg2_range.DateTimeTZRange(now, now))

        self.assertFalse(test_model.range.isempty)
        self.assertNotEqual(test_model.range, empty_range)

        test_model.save()
        test_model.refresh_from_db()

        self.assertTrue(test_model.range.isempty)
        self.assertEqual(test_model.range, empty_range)
