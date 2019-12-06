from django.shortcuts import render


def sign_in(request):
    return render(request, 'sign_in_main.html', {})


def success(request):
    return render(request, 'sign_in_success.html', {})
