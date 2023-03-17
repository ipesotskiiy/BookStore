import os

import pytest

from tests.settings import BASE_DIR

pytest_plugins = [
    "tests.fixtures.user_fixtures",
    "tests.fixtures.product_fixtures",
]


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }


@pytest.fixture()
@pytest.mark.django_db
def create_super_user(django_user_model, get_data_login_super_user):
    return django_user_model.objects.create_superuser(**get_data_login_super_user)
