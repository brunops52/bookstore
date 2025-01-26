from django.test import TestCase
from .factories import UserFactory, OrderFactory

class user_model_test(TestCase):
    def test_user_creation(self):
        user = UserFactory()

        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.username)


    def test_order_creation(self):
        order = OrderFactory()

        self.assertIsNotNone(order.user)
        self.assertIsNotNone(order.product)

