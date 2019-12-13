from django.shortcuts import render, redirect
from main.settings import DEBUG
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib import messages


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"Successsfully signed in as {username}")
                return redirect("sign-in-success")
        else:
            messages.add_message(request, messages.WARNING, "Invalid user credentials!")

    return render(request, 'sign_in_main.html', {'DEBUG': DEBUG, "DEBUG_INFO": request.POST})


def success(request):
    return render(request, 'sign_in_success.html', {})
