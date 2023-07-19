from django.contrib import admin
from .models import *

# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
    'tittle',
    'description',
    'proj_img',
    'date_created',
)
    
    search_fields = ('tittle', 'description', 'proj_img')    
    list_filter = ( 'tittle','description', 'proj_img', )
    
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
    'tittle',
    'file',
    'date_created',
)
    
    search_fields = ('tittle', 'file', 'date_created')    
    list_filter = ( 'tittle','file', 'date_created', )
    
    
    
admin.site.register( Portfolio, PortfolioAdmin)
admin.site.register( Resume, ResumeAdmin)