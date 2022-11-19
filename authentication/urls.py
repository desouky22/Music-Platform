from django.urls import path, include
from . import views
from knox.views import LoginView, LogoutAllView, LogoutView



urlpatterns = [
    path("register/", views.Register.as_view()),
    path("login/", views.Login.as_view()),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', LogoutAllView.as_view(), name='knox_logoutall'),
]
