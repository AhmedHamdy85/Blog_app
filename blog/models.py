from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT= 'DF', 'Draft'
        PUBLISHED= 'PB' , 'Published'

    title = models.CharField(max_length=100)
    body= models.TextField()
    slug=models.SlugField(blank=True,max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish= models.DateTimeField(default=timezone.now)
    status= models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return f'this post title is {self.title}'
