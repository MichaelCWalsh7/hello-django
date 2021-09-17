from django.test import TestCase
from .models import Item


# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        # set an http request for the home page as a variable
        response = self.client.get('/')
        # checks is the response status is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # ensure the correct template is being used
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # sets  an http request for the add item page as a variable
        response = self.client.get('/add')
        # checks is the response status is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # ensure the correct template is being used
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # creates a test item
        # pylint: disable=maybe-no-member
        item = Item.objects.create(name='Test todo item')
        # set an http request for the test item's page as a variable
        # note this is different from above becasue the edit page will always
        # have a unique id and this is the most robust way around that
        response = self.client.get(f'/edit/{item.id}')
        # checks is the response status is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # ensure the correct template is being used
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # intialize a variable that acts as if we've submitted the item form
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # if add is successful, the app should redirect, so testing the
        # redirection is a good way to test the add
        # test if item creation ends in reidirect to home
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # create an item to be deleted
        # pylint: disable=maybe-no-member
        item = Item.objects.create(name='Test todo item')
        # delete item using item's id
        response = self.client.get(f'/delete/{item.id}')
        # again a crud operation is tested using it's redirect
        self.assertRedirects(response, '/')
        # another way to test is to filter items by the id of the item that
        # has just been deleted
        # filter items by delted id
        # pylint: disable=maybe-no-member
        existing_items = Item.objects.filter(id=item.id)
        # ensure item is delted by checking if filtered list length = 0
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # create an item to be toggled
        # pylint: disable=maybe-no-member
        item = Item.objects.create(name='Test todo item', done=True)
        # toggle item using item's id
        response = self.client.get(f'/toggle/{item.id}')
        # again a crud operation is tested using it's redirect
        self.assertRedirects(response, '/')
        # get updated item
        # pylint: disable=maybe-no-member
        updated_item = Item.objects.get(id=item.id)
        # check if item has indeed been updated
        self.assertFalse(updated_item.done)
