from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('internshipdetails/', views.internshipdetails, name='internshipdetails'),
    
    
    path('contacts/', views.contacts, name='contacts'),
    path('testimonial/', views.testimonial, name='testimonial'),
    
    
]