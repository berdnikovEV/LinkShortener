from django.db import models
from .utils import get_new_code


class ShortenedLink(models.Model):
    initial_url = models.CharField(max_length=100)
    short_code = models.CharField(max_length=6, unique=True)

    tags = models.CharField(max_length=100)
    owner_username = models.CharField(max_length=32)

    def __str__(self):
        return str(self.short_code)

    def save(self, *args, **kwargs):
        self.short_code = get_new_code(self) \
                            if not self.short_code \
                            else self.short_code
        super(ShortenedLink, self).save(*args, **kwargs)
