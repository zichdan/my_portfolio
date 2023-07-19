from django.shortcuts import render, redirect
from django.contrib import messages
from myproject.models import Portfolio

# Create your views here.



def portfolio(request):
    
    
    projects = Portfolio.objects.all() # select * from projects
    context = {
        "projects": projects
    }
    return render(request, 'portfolio.html', context)



def project_detail(request, project_id):
    projects = Portfolio.objects.get(pk=project_id)
    
    
    context = {"projects": projects}
    return render(request, "project_detail.html",context)