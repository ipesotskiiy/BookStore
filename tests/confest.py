import pytest


@pytest.fixture()
def create_super_user(django_user_model, get_data_login_super_user):
    return django_user_model.objects.create_superuser(**get_data_login_super_user)
