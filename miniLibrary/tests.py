from django.test import TestCase
from miniLibrary.models import User,Book, Order

# Create your tests here.

class SimpleTest(TestCase):
    def test_index_access(self):
        response = self.client.get('/miniLibrary/books/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/miniLibrary/books/login/')
        self.assertEqual(response.status_code, 200)

    def test_create_user_access(self):
         response = self.client.get('/miniLibrary/books/user/registration/')
         self.assertEqual(response.status_code, 200)

    def test_create_user_access(self):
         response = self.client.post('/miniLibrary/books/user/registration/',{'username' : 'alexandraC','password':'1234567890', 'password_match':'1234567890'})
         self.assertEqual(response.status_code, 302)

    def test_login(self): 
        user = User(username = 'alexandraC', password = '1234567890')
        user.save()
        response = self.client.post('/miniLibrary/books/login/',{'username' : 'alexandraC','password':'1234567890'})
        self.assertEqual(response.status_code, 302)

    def test_create_user(self):
        response = self.client.post('/miniLibrary/books/user/registration/',{'username' : 'alexandraC','password':'1234567890', 'password_match':'1234567890'})
        user = User.objects.get(username = 'alexandraC')
        self.assertEqual(user is None, False)

    def test_book_detail(self):
        book = Book (name = 'Title', author = 'Jake T.', description = 'description', publisher = 'Tei', price = '11.1')
        book.save()
        response = self.client.get('/miniLibrary/books/1/')
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):  
        user = User(username = 'ale', password = '1234')
        user.save()
        response = self.client.post('/miniLibrary/books/login/',{'username' : 'ale','password':'1234'})
        response = self.client.post('/miniLibrary/books/add/',{'name' : 'Title', 'author' : 'Jake T.', 'description' : 'description', 'publisher' : 'Tei', 'price' : '11.1'})
        book = Book.objects.get(name = 'Title')
        self.assertEqual(book is None, False)

    def test_delete_book(self):  
        user = User(username = 'ale', password = '1234')
        user.save()
        response = self.client.post('/miniLibrary/books/login/',{'username' : 'ale','password':'1234'})
        book = Book (name = 'Title', author = 'Jake T.', description = 'description', publisher = 'Tei', price = '11.1')
        book.save()
        response = self.client.post('/miniLibrary/books/1/delete',{'name' : 'Title', 'author' : 'Jake T.', 'description' : 'description', 'publisher' : 'Tei', 'price' : '11.1'})
        book = Book.objects.get(name = 'Title')
        self.assertEqual(book is None, False)

    def test_update_book(self):  
        user = User(username = 'ale', password = '1234')
        user.save()
        response = self.client.post('/miniLibrary/books/login/',{'username' : 'ale','password':'1234'})
        book = Book (name = 'Title', author = 'Jake T.', description = 'description', publisher = 'Tei', price = '11.1')
        book.save()
        response = self.client.post('/miniLibrary/books/1/update',{'description' : 'new description', 'price' : '12.1'})
        book = Book.objects.get(name = 'Title')
        self.assertEqual(book.description == 'New description' and book.price == '12.1', False)

    def test_order_book(self):
        user = User(username = 'ioana', password = '1234')
        user.save()
        response = self.client.post('/miniLibrary/books/login/',{'username' : 'ioana','password':'1234'})
        bookToBuy = Book (name = 'Title', author = 'Jake T.', description = 'description', publisher = 'Tei', price = '11.1')
        bookToBuy.save()
        response = self.client.post('/miniLibrary/books/1/add/')
        response = self.client.post('/miniLibrary/books/order/')
        order = Order.objects.get (bookId = bookToBuy)
        self.assertEqual(order is None, False)

    
        


   
