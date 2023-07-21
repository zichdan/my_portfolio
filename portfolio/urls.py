from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('testimonial/', views.testimonial, name='testimonial'),
    
    
    path('internshipdetails/', views.internshipdetails, name='internshipdetails'),
    
    
    
    
]