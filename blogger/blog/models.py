from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
        Title=models.CharField(max_length=100)
        Slug=models.SlugField(max_length=100)
        body=models.TextField()

        
        publish=models.DateTimeField(default=timezone.now)
        created=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)

        

    

    