import pytest

from tests.settings import (
    TEST_SUPER_USER_EMAIL,
    TEST_SUPER_USER_PASSWORD
)


@pytest.fixture()
def get_data_login_super_user():
    data_form_login_super_user = {
        'email': TEST_SUPER_USER_EMAIL,
        'password': TEST_SUPER_USER_PASSWORD
    }
    return data_form_login_super_user
