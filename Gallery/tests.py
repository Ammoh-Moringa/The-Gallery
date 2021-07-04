from django.test import TestCase

from .models import Image, Category, Location

# Create your tests here.

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Barcelona')
        self.location.save_location()

        self.category = Category(name='Sports')
        self.category.save_category()

        self.image_test = Image(id=1, name='Barcelona', description='Barcelona football club', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)
