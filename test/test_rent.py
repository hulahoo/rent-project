from django.urls import reverse

from mixer.backend.django import mixer
from faker import Faker
import pytest

from rent_app.models import Rental, Reservation

faker = Faker()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, status_code", [
        pytest.param(
            "RENT", 201
        )
    ]
)
def test_create_rent(name, status_code, api_client):
    url = reverse("rent-list")
    data = {
        "name": name
    }
    response = api_client.post(url, data=data)
    assert response.status_code == status_code


@pytest.mark.django_db
@pytest.mark.parametrize(
    "checkin, checkout", [
        pytest.param(
            faker.date_this_year(), faker.date_this_year()
        ),
        pytest.param(
            faker.date_this_year(), faker.date_this_year()
        ),
    ]
)
def test_create_reservation(checkin, checkout):
    rents = mixer.cycle(2).blend(Rental, name=(name for name in ('RENT-1', 'RENT-2')))
    data = {
        "checkin": checkin,
        "checkout": checkout,
    }
    reserv = mixer.cycle(2).blend(
        Reservation, checkin=data.get("checkin"),
        checkout=data.get("checkout"), rental_id=(rent for rent in rents)
    )
    assert reserv[0].rental_id in (rent for rent in rents)
