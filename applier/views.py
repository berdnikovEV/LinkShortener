from django.shortcuts import render
from shorten.models import ShortenedLink


def applier(request, short_code=''):
    link = ShortenedLink.objects.filter(short_code=short_code)
    if link.exists():
        obj = link[0]

        context = {
            'is_valid': 'Valid',
            'destination': obj.initial_url
        }

        obj.usage_count += 1
        obj.save()

        return render(request, 'applier.html', context)
    else:
        context = {
            'is_valid': '',
            'exc': str('Error: link not found')
        }
        return render(request, 'applier.html', context)


def link_info(request, short_code=''):
    link = ShortenedLink.objects.filter(short_code=short_code)

    if link.exists():
        obj = link[0]
        if request.method == 'POST':
            obj.description = request.POST['description']
            obj.tags = request.POST['url_tags'].split(sep=', ')
            obj.save()

        is_owner = (obj.owner_username == request.user.username)

        context = {
            'is_valid': 'Valid',
            'is_owner': is_owner,
            'description': obj.description,
            'tag_list': obj.tags,
            'tag_text': ', '.join(obj.tags)
        }
        return render(request, 'link_info.html', context)
    else:
        context = {
            'is_valid': '',
            'exc': str('Error: link not found')
        }
        return render(request, 'link_info.html', context)
