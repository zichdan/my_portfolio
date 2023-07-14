from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    posts = Blogs.objects.all()
    
    context = {
        "posts": posts
    }
    return render(request, 'blog.html', context )


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('num')
        desc = request.POST.get('desc')
        
        query = Contact(name=name, email=email, phonenumber=phonenumber, description=desc)
        query.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        
        return redirect('/contact')
        
    
    return render(request, 'contact.html')


