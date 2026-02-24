from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .import views

urlpatterns = [
    path("token/", views.UserLoginAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', views.UserLogoutAPIView.as_view()),
    path('register/', views.UserRegisterAPIView.as_view()),
    path('register/verify/', views.UserRegiterVerifyCodeAPIView.as_view()),
]
