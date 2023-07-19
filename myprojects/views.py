from django.shortcuts import render, redirect
from django.contrib import messages
from myprojects.models import  Portfolio

# Create your views here.



def portfolio(request):
    
    
    return render(request, 'portfolio.html')



