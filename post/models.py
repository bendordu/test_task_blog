from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', blank=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
            return self.title

    def get_absolute_url(self):
            return reverse('post:post', args=[self.id, self.slug])

