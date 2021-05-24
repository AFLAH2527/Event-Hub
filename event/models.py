from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=30)
    max_participants = models.IntegerField()
    content = models.TextField()
    banner = models.ImageField(default='banner.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Join(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('user-events', kwargs={'username': self.username})