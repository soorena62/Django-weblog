from django.db import models
from django.shortcuts import reverse


# Create your models here:


class Post(models.Model):

    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('pub', 'Published')
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail_view',  args={self.pk})



