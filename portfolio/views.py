from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from myproject.models import *



# Create your views here.

def home(request):
    resumes = Resume.objects.all()
    
    context = {
        "resumes": resumes
    }
    
    return render(request, 'home.html', context)



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
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create a new Contact object and save it to the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Additional logic: Send an email to the site admin
        send_mail(
            'New Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}',
            'ezichdan@gmail.com',  # Replace with the admin email address
            ['ezichdan@gmail.com'],  # Replace with the admin email address
            fail_silently=True,
        )
        messages.success(request, 'Your message has been sent. Thank you!')
        
        
        return redirect('/contact')
    return render(request, 'contact.html')




def contacts(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        query = Contact(name=name, email=email, subject=subject, message=message,)
        query.save()
        messages.success(request, 'Your message has been sent. Thank you!')
        
        return redirect('/contacts')
    return render(request, 'contacts.html')












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





# # views.py

# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.core.mail import send_mail
# from .models import Contact

# def contact_submit(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Validation logic
#         if not name or not email or not subject or not message:
#             return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

#         # Additional validation for email
#         if '@' not in email or '.' not in email:
#             return JsonResponse({'status': 'error', 'message': 'Invalid email format.'})

#         # Create a new Contact object and save it to the database
#         contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)

#         # Additional logic: Send an email to the site admin
#         send_mail(
#             'New Contact Form Submission',
#             f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}',
#             'admin@example.com',  # Replace with the admin email address
#             ['admin@example.com'],  # Replace with the admin email address
#             fail_silently=True,
#         )

#         # Additional logic: Send a confirmation email to the user (optional)
#         # send_mail(
#         #     'Confirmation of Your Contact Form Submission',
#         #     'Thank you for contacting us. We have received your message.',
#         #     'admin@example.com',  # Replace with the site's email address
#         #     [email],  # Use the user's email address for the recipient
#         #     fail_silently=True,
#         # )

#         # Return a success message as a JSON response
#         return JsonResponse({'status': 'success', 'message': 'Your message has been sent. Thank you!'})

#     # If the request method is not POST, display the form
#     return render(request, 'contact_form.html')  # Replace 'contact_form.html' with the template name that contains the form.





