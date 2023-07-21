from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

# Custom form for ProjectAdmin
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'category': forms.RadioSelect(),  # Use RadioSelect widget for the category field
        }


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
    'category',
)
    
    search_fields = ('category',)    
    list_filter = ( 'category', )
    

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
    'tittle',
    'description',
    'proj_img1',
    'date_created',
)
    form = ProjectAdminForm
    filter_horizontal = ('category',)  # Display the category field as a checkbox select multiple
    
    search_fields = ('tittle', 'description', 'proj_img1')    
    list_filter = ( 'tittle','description', 'proj_img1', )
    
    
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
    'tittle',
    'file',
    'date_created',
)
    
    search_fields = ('tittle', 'file', 'date_created')    
    list_filter = ( 'tittle','file', 'date_created', )
    
    
    
admin.site.register( Category, CategoryAdmin)
admin.site.register( Project, ProjectAdmin)
admin.site.register( Resume, ResumeAdmin)