from django.shortcuts import render
from shorten.models import ShortenedLink


def applier(request, short_code=''):
    link = ShortenedLink.objects.filter(short_code=short_code)
    if link.exists():
        context = {
            'is_valid': "Valid",
            'destination': link[0].initial_url,
            'tag_list': link[0].tags
        }
        return render(request, 'applier.html', context)
    else:
        context = {
            'is_valid': '',
            'exc': str('Error: link not found')
        }
        return render(request, 'applier.html', context)
