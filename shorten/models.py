from django.db import models
from .utils import get_new_code


class ShortenedLink(models.Model):
    initial_url = models.CharField(max_length=100)
    shortened_url = models.CharField(max_length=5, unique=True)

    tags = models.CharField(max_length=100)
    owner_username = models.CharField(max_length=32)

    def __str__(self):
        return str(self.shortened_url)

    def save(self, *args, **kwargs):
        self.shortened_url = get_new_code(self) \
                            if not self.shortened_url \
                            else self.shortened_url
        super(ShortenedLink, self).save(*args, **kwargs)
