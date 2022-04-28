from django.conf import settings

import pytest


@pytest.fixture(scope="module")
def django_db_setup():
    settings.DATABASES["default"] = {
        "NAME": "test_db",
        "ENGINE": "django.db.backends.postgresql",
    }


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
