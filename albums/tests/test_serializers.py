import pytest
from rest_framework import status
from albums.models import Album
from users.models import User
from artists.models import Artist


@pytest.mark.django_db
def test_get_all_albums(client):
    user = User.objects.create_user(
        username="admin", email="admin@gmail.com", password="admin@123456789"
    )
    artist = Artist()
    artist.user = user
    artist.stage_name = "tamer Ashour"
    artist.social_link = "tamer.com"
    artist.save()

    album = Album()
    album.artist = artist
    album.name="Ayam"
    album.cost=1500
    album.release_datetime = "2022-11-11"
    album.save()
    response = client.get("/albums/")

    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert data.get("id") == album.id
    assert data.get("name") == album.name
    assert data.get("release_datetime") == album.release_datetime
    assert data.get("cost") == album.cost
    assert data.get("artist")["id"] == artist.id
    assert data.get("artist")["stage_name"] == artist.stage_name
    assert data.get("artist")["social_link"] == artist.social_link
