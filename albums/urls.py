from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.AlbumList.as_view()),
    path("manualFilter/", views.AlbumListAddingManualFiltering.as_view()),
    path("test/", views.send_emails)
]
