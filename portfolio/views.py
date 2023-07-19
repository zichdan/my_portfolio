from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs, Internship

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

def testimonial(request):
    return render(request, 'testimonial.html')




def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please Login to access this page')
        return redirect('/auth/login/')
        
    if request.method=='POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        usn = request.POST.get('usn')
        college_name = request.POST.get('cname')
        offer = request.POST.get('offer')
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        projreport = request.POST.get('projreport')
        
        #converting to upper case letters before saving
        fullname = fullname.upper()
        usn = usn.upper()
        college_name = college_name.upper()
        offer = offer.upper()
        projreport = projreport.upper()
        
        # data validation checking if usn or email is already registered
        
        check1 = Internship.objects.filter(usn=usn)
        check2 = Internship.objects.filter(email=email)
        
        if check1 or check2:
            messages.warning(request, 'This usn or email is already registered')
            return redirect('internshipdetails')
        
        query = Internship(fullname=fullname, email=email, usn=usn, college_name=college_name, offer_status=offer, start_date=start_date, end_date=end_date, proj_report=projreport )
        query.save()
        messages.success(request, 'Form is submitted Succesfully!')
        return redirect('internshipdetails')
    
    return render(request, 'intern.html')


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

def contacts(request):
    # if request.method=='POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phonenumber = request.POST.get('num')
    #     desc = request.POST.get('desc')
        
    #     query = Contact(name=name, email=email, phonenumber=phonenumber, description=desc)
    #     query.save()
    #     messages.success(request, 'Your message has been sent. Thank you!')
        
    #     return redirect('/contact')
        
    
    return render(request, 'contacts.html')


