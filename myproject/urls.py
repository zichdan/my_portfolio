from django.urls import path, re_path  # Import re_path instead of url
from myproject import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('proj_details/<str:pk>/', views.proj_details, name='proj_details'),
    path('resume/', views.resume, name='resume'),
    re_path(r"^download/(?P<path>.*)$", serve, {'document_root': settings.MEDIA_ROOT}),
    
    
    # path('download/<str:path>/', views.download, name='download'),    
]
