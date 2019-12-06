from django.shortcuts import render


def shorten(request):
    return render(request, 'shorten_main.html', {})


def success(request):
    return render(request, 'shorten_success.html', {})
