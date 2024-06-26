from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f"Welcome Back, {username}"))
            return redirect("home")

    return render(request, "login.html", {})

def logout_user(request):
    username = request.user
    logout(request)
    messages.success(request, (f"See You Soon, {username}"))
    return redirect("home")

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!!"))
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
