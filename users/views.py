# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"You Have Successfully Registered...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username or Password Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"You have Successfully Logged In")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"You have Successfully Logged Out")
    return redirect("index")
