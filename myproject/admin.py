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
    
admin.site.register( Portfolio, PortfolioAdmin)