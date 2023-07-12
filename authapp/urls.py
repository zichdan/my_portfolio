from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.authlogin, name='login'),
    path('logoout/', views.authlogout, name='logout'),
]