from django.urls import path
from user.views import (
    UserDetailView,
    UserCreateView,
    UserLoginView,
    UserUpdateView,
    UserListView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("list/", UserListView.as_view(), name="user_list"),
]
