from django.db import models

from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=2000)
    # image = models.ImageField(upload_to="%Y/%m/%d")
    image_url = models.URLField(verbose_name=None)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(blank=True, null=True)



