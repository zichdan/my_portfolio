from django.urls import path
from myproject import views


urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
]