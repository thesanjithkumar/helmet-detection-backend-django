from django.db import models
from django.utils import timezone

# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now())
    location = models.TextField()
    image = models.ImageField(upload_to='fine_images', blank=True)

    def __str__(self):
        return self.title
