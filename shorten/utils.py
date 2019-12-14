import rstr


def get_new_code(obj):
    code = rstr.xeger(r'[a-zA-Z0-9]{6}')
    ShortenedLink = obj.__class__

    if ShortenedLink.objects.filter(shortened_url=code).exists():
        return get_new_code(obj)

    return code
