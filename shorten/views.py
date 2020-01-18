from django.shortcuts import render, redirect
from .models import ShortenedLink
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/sign_in')
def shorten(request):
    if request.method == 'POST':
        init_url = request.POST['initial_url']
        description = request.POST['description']
        tags = request.POST['url_tags']
        user = request.user
        tag_list = tags.split(sep=', ')
        url_obj = ShortenedLink(owner_username=user,
                                initial_url=init_url,
                                description=description,
                                tags=tag_list,
                                usage_count=0)
        url_obj.save()
        messages.add_message(request, messages.SUCCESS, f"Successsfully shortened {url_obj.initial_url} to {url_obj.short_code}")
        return redirect('shorten-success')
    return render(request, 'shorten_main.html', {})


def success(request):
    return render(request, 'shorten_success.html', {})
