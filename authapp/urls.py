from django.urls import path
from authapp import views

urlpatterns = [
    path('auth/signup/', views.signup, name='signup'),
    path('auth/login/', views.authlogin, name='login'),
    path('auth/logoout/', views.logout, name='logout'),
]