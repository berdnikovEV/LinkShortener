from django.shortcuts import render
from shorten.models import ShortenedLink


def applier(request, short_code=''):
    link = ShortenedLink.objects.filter(short_code=short_code)
    if link.exists():
        obj = link[0]

        context = {
            'is_valid': 'Valid',
            'destination': obj.initial_url,
            'tag_list': obj.tags
        }
        obj.usage_count += 1
        obj.save()
        link[0].save()
        return render(request, 'applier.html', context)
    else:
        context = {
            'is_valid': '',
            'exc': str('Error: link not found')
        }
        return render(request, 'applier.html', context)
