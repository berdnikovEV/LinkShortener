from django.shortcuts import render
from .models import ShortenedLink
from django.contrib.auth.decorators import login_required


@login_required(login_url='/sign_in')
def shorten(request):
    if request.method == 'POST':
        init_url = request.POST['initial_url']
        tags = request.POST['url_tags']
        user = request.user
        init_url
        str(user)
        url_obj = ShortenedLink(owner_username=user,
                                initial_url=init_url,
                                tags=tags)
        url_obj.save()
    return render(request, 'shorten_main.html', {})


def success(request):
    return render(request, 'shorten_success.html', {})
