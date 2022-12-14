
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_Post", views.newPost, name="new_Post"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("edit/<int:post>", views.edit, name="edit"),
    path("like/<int:postID>", views.like, name="like"),
    path("following", views.following_Site, name="following_Site"),

]
