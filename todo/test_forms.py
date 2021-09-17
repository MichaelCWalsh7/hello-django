from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # tests that the name field is required
    def test_item_name_is_required(self):
        # initialize a form without a name to simulate a similar user action
        form = ItemForm({'name': ''})
        # tests that form is not valid
        self.assertFalse(form.is_valid())
        # shows that error occured in the name field
        self.assertIn('name', form.errors.keys())
        # checks error message is as expected
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        # note that in the above two lines we are checking the error message
        # that gets returned in a dictionary (of lists??)

    # tests that the done field is not required
    def test_done_is_not_required(self):
        # initialize a form with a placeholder name and no 'done' status
        form = ItemForm({'name': 'Test todo item'})
        # test if form is valid
        self.assertTrue(form.is_valid())

    # tests that form is only displaying required information to the user
    def test_fields_are_explicit_in_form_metaclass(self):
        # initialize an empty form
        form = ItemForm()
        # test that the fields are only those that we have specified
        self.assertEqual(form.Meta.fields, ['name', 'done'])
