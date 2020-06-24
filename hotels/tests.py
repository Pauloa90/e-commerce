from django.test import TestCase
from .models import Hotel

# Create your tests here.
class HotelTests(TestCase):
    """
    Here We'll define the tests that will run against our Post models 
    """

    def test_str(self):
        test_name = Hotel(name='A hotel')
        self.assertEqual(str(test_name), 'A hotel')