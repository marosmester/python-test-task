from django.db import models

# Create your models here.

class BlogPost(models.Model):
    userId = models.IntegerField(default=0)
    title = models.CharField(max_length= 100)
    body = models.CharField(max_length= 2000)

    def __str__(self):
        return self.title

