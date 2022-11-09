from rest_framework import status
import pytest
from users.models import User


@pytest.mark.django_db
def test_register(client):
    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "admin@123456789",
        "password2": "admin@123456789",
    }

    response = client.post("/authentication/register/", user)

    assert response.status_code == status.HTTP_201_CREATED

    assert "username" in response.data
    assert response.data["username"] == user["username"]

    assert "email" in response.data
    assert response.data["email"] == user["email"]


@pytest.mark.django_db
def test_register_no_username(client):
    user = {
        "username": "",
        "email": "admin@gmail.com",
        "password": "admin",
        "password2": "admin",
    }

    response = client.post("/authentication/register/", user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert "username" in response.data
    assert response.data["username"] != user["username"]


@pytest.mark.django_db
def test_register_no_email(client):
    user = {
        "username": "admin",
        "email": "",
        "password": "admin",
        "password2": "admin",
    }
    response = client.post("/authentication/register/", user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert "email" in response.data
    assert response.data["email"] != user["email"]


@pytest.mark.django_db
def test_register_no_password1(client):
    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "",
        "password2": "admin",
    }
    response = client.post("/authentication/register/", user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert "password" in response.data
    assert response.data["password"] != user["password"]


@pytest.mark.django_db
def test_register_no_password2(client):
    user = {
        "username": "admin",
        "email": "admin@gmail.com",
        "password": "admin",
        "password2": "",
    }
    response = client.post("/authentication/register/", user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    assert "password2" in response.data
    assert response.data["password2"] != user["password2"]


@pytest.mark.django_db
def test_login_user_succes(client):
    User.objects.create_user(username="admin", email="admin@gmail.com", password="admin@123456789")
    data = {"username": "admin", "password": "admin@123456789"}
    response = client.post("/authentication/login/", data)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_user_no_username(client):
    data = {"username": "", "password": "admin"}
    response = client.post("/authentication/login/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_user_no_password(client):
    data = {"username": "admin", "password": ""}
    response = client.post("/authentication/login/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_user_wrong_password(client):
    data = {"username": "admin", "password": "helloworld"}
    response = client.post("/authentication/login/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_user_wrong_username(client):
    data = {"username": "desouky", "password": "admin@123456789"}
    response = client.post("/authentication/login/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
