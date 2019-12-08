from django.shortcuts import render, redirect
from main.settings import DEBUG
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib import messages


def register(request):
    if request.method == "POST":

        current_user_login_list = (user.username for user in User.objects.all())
        current_user_email_list = (user.email for user in User.objects.all())
        
        login = request.POST['login'] 
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if '' in (login, email, password):
            messages.add_message(request, messages.WARNING, "All fields must be filled")
            return render(request, 'register_main.html', {'login':login, 'email':email})


        if password !=  password_confirmation:
            messages.add_message(request, messages.WARNING, "Password didn't match its confirmation")
            return render(request, 'register_main.html', {'login':login, 'email':email})

        if email not in current_user_email_list and login not in current_user_login_list:
            user = User.objects.create_user(login, email=email, password=password)
            user.save()
            return redirect("register-success")
        else:
            messages.add_message(request, messages.WARNING, "You are already registered!")

    return render(request, 'register_main.html', {})


def success(request):
    return render(request, 'register_success.html', {})
