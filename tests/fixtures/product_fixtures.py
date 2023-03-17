# import pytest
import pytest

from tests.settings import (
    TEST_BOOK_GENRE,
    TEST_BOOK_TITLE,
    TEST_BOOK_AUTHOR,
    TEST_BOOK_PRICE,
    TEST_BOOK_COVER,
    TEST_BOOK_DATE_OF_ISSUE,
    TEST_BOOK_IN_STOCK,
    TEST_BOOK_DESCRIPTION
)


@pytest.fixture()
def get_book_data():
    data_from_book = {
        'genre': TEST_BOOK_GENRE,
        'title': TEST_BOOK_TITLE,
        'author': TEST_BOOK_AUTHOR,
        'price': TEST_BOOK_PRICE,
        'cover': TEST_BOOK_COVER,
        'date_of_issue': TEST_BOOK_DATE_OF_ISSUE,
        'in_stock': TEST_BOOK_IN_STOCK,
        'description': TEST_BOOK_DESCRIPTION
    }
    return data_from_book
