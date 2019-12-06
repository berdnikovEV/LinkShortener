from django.shortcuts import render


def register(request):
    return render(request, 'register_main.html', {})


def success(request):
    return render(request, 'register_success.html', {})
