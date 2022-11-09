import pytest
from users.models import User
from rest_framework import status


@pytest.mark.django_db
def test_get_user_unauthenticated(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    user = User.objects.get(username="admin")
    response = client.get(f"/users/{user.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert user.id == response.data["id"]
    assert user.username == response.data["username"]
    assert user.email == response.data["email"]
    assert user.bio == response.data["bio"]


@pytest.mark.django_db
def test_put_user_unauthenticated(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )

    user = User.objects.get(username="admin")
    data = {
        "username": "desouky22",
        "email": "desouky@gmail.com",
        "bio": "hello its me",
    }
    response = client.put(f"/users/{user.id}/", data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_user_authenticated(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    user = {"username": "admin", "password": "admin@123456789"}
    login_response = client.post("/authentication/login/", user)
    user_id = login_response.data["User"]["id"]
    response = client.get(f"/users/{user_id}/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_put_user_authenticated_and_the_current_user(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    user = {"username": "admin", "password": "admin@123456789"}
    login_response = client.post("/authentication/login/", user)
    user_id = login_response.data["User"]["id"]
    token = login_response.data["Knox Token"]
    data = {
        "username": "desouky22",
        "email": "desouky@gmail.com",
        "bio": "hello its me",
    }
    client.credentials(HTTP_AUTHORIZATION="Token " + token)
    response = client.put(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_put_user_authenticated_not_the_current_user(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    User.objects.create_user(
        username="admin2", email="admin2@gmail.com", password="admin2@123456789"
    )

    user = {"username": "admin2", "password": "admin2@123456789"}
    login_response = client.post("/authentication/login/", user)
    token = login_response.data["Knox Token"]
    data = {
        "username": "desouky22",
        "email": "desouky@gmail.com",
        "bio": "hello its me",
    }
    user_id = User.objects.get(username="admin").id
    client.credentials(HTTP_AUTHORIZATION="Token " + token)
    response = client.put(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_put_user_unauthenticated(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )

    data = {
        "username": "desouky22",
        "email": "desouky@gmail.com",
        "bio": "hello its me",
    }
    user_id = User.objects.get(username="admin").id
    response = client.put(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_patch_user_authenticated_and_the_current_user(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    user = {"username": "admin", "password": "admin@123456789"}
    login_response = client.post("/authentication/login/", user)
    user_id = login_response.data["User"]["id"]
    token = login_response.data["Knox Token"]
    data = {
        "username": "desouky22",
        "bio": "hello its me",
    }
    client.credentials(HTTP_AUTHORIZATION="Token " + token)
    response = client.patch(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_patch_user_authenticated_not_the_current_user(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    User.objects.create_user(
        username="admin2", email="admin2@gmail.com", password="admin2@123456789"
    )

    user = {"username": "admin2", "password": "admin2@123456789"}
    login_response = client.post("/authentication/login/", user)
    token = login_response.data["Knox Token"]
    data = {
        "username": "desouky22",
        "bio": "hello its me",
    }
    user_id = User.objects.get(username="admin").id
    client.credentials(HTTP_AUTHORIZATION="Token " + token)
    response = client.patch(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_patch_user_unauthenticated(client):
    User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )

    data = {
        "username": "desouky22",
        "email": "desouky@gmail.com",
        "bio": "hello its me",
    }
    user_id = User.objects.get(username="admin").id
    response = client.patch(f"/users/{user_id}/", data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
