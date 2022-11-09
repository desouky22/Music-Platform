import pytest
from rest_framework.test import APIClient
from users.models import User


@pytest.fixture
def auth_client():
    def authenticate(user=None):
        client = APIClient()
        if user is None:
            try:
                user = User.objects.first()
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username="desouky22", password="oed123456789"
                )

        response = client.post(
            "/login/", username=user.username, password=user.password
        )
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="Token " + token)
        return client

    return authenticate


@pytest.fixture
def client():
    return APIClient()
