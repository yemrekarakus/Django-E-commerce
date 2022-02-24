from distutils.command.upload import upload
from django.db import models
from autoslug import AutoSlugField

DEFAULT_STATUS = "draft"

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlanmis'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    title = models.CharField(max_length=180)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page', null=True)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=12,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)   
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   