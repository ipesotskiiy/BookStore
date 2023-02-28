from product.models import Book
import pytest


@pytest.mark.django_db
def test_book_view():
    books = Book.objects.all()
    response = books.get(path='/book/all', format='json')
    assert response.status_code == 200