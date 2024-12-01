from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Set up initial data for the tests
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Sample Book", publication_year=2023, author=self.author
        )

    def test_create_book(self):
        # Test creating a new book
        response = self.client.post(
            '/api/books/',
            {
                "title": "New Book",
                "publication_year": 2024,
                "author": self.author.id,
            },
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_books(self):
        # Test retrieving all books
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_get_book_detail(self):
        # Test retrieving a single book
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        response = self.client.put(
            f'/api/books/{self.book.id}/',
            {
                "title": "Updated Title",
                "publication_year": 2023,
                "author": self.author.id,
            },
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Book.objects.all()), 0)

    def test_filter_books_by_author(self):
        # Test filtering books by author
        response = self.client.get(f'/api/books/?author__name={self.author.name}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["author"], self.author.name)

    def test_search_books(self):
        # Test searching books by title
        response = self.client.get(f'/api/books/?search=Sample')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Sample Book")
