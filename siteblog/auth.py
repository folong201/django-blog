# login and register function page
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from siteblog.forms.authform import RegisterForm,LoginForm


def login_view(request):
    msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                msg = 'Login successful'
                login(request, user)
                return redirect('index' )
            else:
                msg = 'Login failedv'
                print(msg,user)
                return redirect('login')
        else:
            print(form.errors)
    else:
        msg = 'Login failed 2'
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})
# similarity

def register_view(request):
    msg = None
    if request.method =='POST':
        form = RegisterForm(request.POST)
        # set the user name
        # form.username = request.POST.get('email')
        if form.is_valid():
            form.save()
            msg = "registration ok"
            print(msg)
            return redirect('login')
        else:
          print("and error occure 1")
            
    else:   
        form = RegisterForm()
        print(form.errors)
        print("and error occure")
    return render(request, 'auth/register.html', {'form': form})
