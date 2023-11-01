from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Account

# Create your views here.
def signup(request) :
    if request.method == 'POST':
        print("INside POST method")
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            print("FOrm is valid")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            if len(password) >=5:
                print("passwod is valid")
                user = Account.objects.create_user(first_name=first_name, email=email,username=username, password=password)
                user.save()
                messages.success(request, "Signup sucessfull!")
                return redirect('login')
            else:
                messages.error(request, 'Password must be greater then 4')
                return redirect('signup')
        else:
            messages.error(request, form.errors)
    else:
        form = forms.SignupForm()
    context = {
        'f': form,
    }
    return render(request,'accounts/signup.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Logged in Failed")
    return render(request, 'accounts/login.html')


def logout(request):
    if request.user != None:
        auth.logout(request)
    return redirect("index")