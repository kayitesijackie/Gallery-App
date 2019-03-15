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

