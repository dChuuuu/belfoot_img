from django.db import models

# Create your models here.


class Images(models.Model):
    image_id = models.BigAutoField(primary_key=True, unique=True)
    article_id = models.TextField()
    image = models.TextField()
    image_name = models.TextField(default=None, unique=True)
    objects = models.Manager

