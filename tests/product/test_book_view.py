from product.models import Book
import pytest


@pytest.mark.django_db
def test_book_view(create_super_user):
    user = create_super_user
    print(user.pk)
    # books_qs = Book.objects.all()
    # assert books_qs == Book.objects.all()

