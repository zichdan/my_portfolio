from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('skills/', views.skills, name='skills'),
    path('internshipdetails/', views.internshipdetails, name='internshipdetails'),
    
    
    path('contacts/', views.contacts, name='contacts'),
    path('testimonial/', views.testimonial, name='testimonial'),
    
    
]