from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['Last_name']
        email = request.POST['email']
        uname = request.POST['user_name']
        pwd = request.POST['Pass']
        cpwd =request.POST['con_pass']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pwd,first_name=first,last_name=last,email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'Password not match')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['pass']
        con_pass=request.POST['con_pass']
        Login=auth.authenticate(username=username,password=password)
        if Login is not None:
            auth.login(request,Login)
            return redirect('/')
        else:
            messages.info(request,'Invalid User')
            return redirect('login')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
