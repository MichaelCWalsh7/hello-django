from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    # test if done status is false by default
    def test_defaults_to_false(self):
        # create item to test
        # pylint: disable=maybe-no-member
        item = Item.objects.create(name='Test todo item')
        # test if done is false by default
        self.assertFalse(item.done)
