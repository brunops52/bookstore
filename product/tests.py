from django.test import TestCase
from .models import Product, Category
from .factories import ProductFactory, CategoryFactory

class Category_model_test(TestCase):
    def test_category_creation(self):
        category = CategoryFactory()

        self.assertIsNotNone(category.title)
        self.assertIsNotNone(category.slug)
        self.assertIsNotNone(category.description)
        self.assertIsNotNone(category.active)

        self.assertEqual(Category.objects.count(), 1)

    def test_product_creation(self):
        product = ProductFactory()

        self.assertIsNotNone(product.price)
        self.assertIsNotNone(product.category)
        self.assertIsNotNone(product.title)

        self.assertEqual(Product.objects.count(), 1)
