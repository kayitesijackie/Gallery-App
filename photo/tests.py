from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        self.food = Category(name = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_category(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.food.delete_category('Food')
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class LocationTestCase(TestCase):
    def setUp(self):
        self.kigali = Location(name = 'Kigali')

    def test_instance(self):
        self.assertTrue(isinstance(self.kigali, Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_location(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self, event = None):
        self.kigali.delete_location('Kigali')
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

