from django.shortcuts import render
from shorten.models import ShortenedLink


def search(request, tag=''):

    link_list = ShortenedLink.objects.filter(tags__contains=[tag])
    if link_list.exists():
        code_list = [link.short_code for link in link_list]
        context = {
            'is_valid': True,
            'tag': tag,
            'code_list': code_list,
        }
        return render(request, 'search.html', context)
    else:
        context = {
            'is_valid': False,
            'exc': str(f'Error: tag {tag} not found')
        }
        return render(request, 'search.html', context)
