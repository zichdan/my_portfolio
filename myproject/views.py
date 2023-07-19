from django.shortcuts import render, redirect
from django.contrib import messages
from myproject.models import Portfolio

# Create your views here.



def portfolio(request):
    
    
    projects = Portfolio.objects.all() # select * from post
    context = {
        "projects": projects
    }
    
    return render(request, 'portfolio.html', context)