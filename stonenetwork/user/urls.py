from django.urls import path
from user.views import UserDetailView, UserCreateView, UserLoginView
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
]  
