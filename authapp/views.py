from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.info(request, "Password Is Not Matching!!!")
            return redirect('/auth/signup')
        
        try:
            if User.objects.get(username=email):
                messages.warning(request, "Email is Taken")
                return redirect('/auth/signup')
        except Exception as identifier:
            pass
        
        user = User.objects.create_user( email, password1, password2)
        try:
            user.save()
            messages.success(request, "User Created Successful, Please Login!")
            return redirect('/auth/login')
        except:
            messages.error(request, "Something Went Wrong")
            return redirect(request, '/auth/login')
    
    return render(request, 'signup.html')
    
    
def authlogin(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        myuser = authenticate(username=email, password=password1)
        
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
    return render (request, 'login.html')
    
    
    

def logout(request):
    return render(request, 'logout.html')


