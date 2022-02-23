from distutils.command.upload import upload
from django.db import models

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayınlanmış'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    title = models.CharField(max_length=180)
    # slug = 
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page')
    status = models.CharField(
        default="draft",
        choices=STATUS,
        max_length=12,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    