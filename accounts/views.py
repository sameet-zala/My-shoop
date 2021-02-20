from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def handlesignup(request):
    
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        age = request.POST['age']
        pass1 = request.POST['password']
        pass2 = request.POST['confirmpassword']

        if pass1!=pass2:
            return HttpResponse('Password do not match')

        myuser =CustomUser.objects.create_user(email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.email = email
        myuser.phone = phone
        myuser.gender = gender
        myuser.age = age
        myuser.confirmpassword = pass2
        
        myuser.save()
        # messages.success(request,"sighenuped succesesful")
        # return HttpResponse('sighn up succesful')  
        return redirect('/')
    else:
        return render(request,'accounts/signup.html')
    
def handlelogin(request):

    if request.method == 'POST':
        
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']

        user = authenticate(email=loginemail,password=loginpassword)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('Invalid Credentials')
    else:
       return render(request,'accounts/login.html')
    
def handlelogout(request):
    logout(request)
    messages.success(request,'logout success')
    return redirect('/')
