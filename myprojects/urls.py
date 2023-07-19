from django.urls import path
from myprojects import views


urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    
    
]