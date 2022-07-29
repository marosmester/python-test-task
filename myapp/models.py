from django.db import models

# Models start HERE

class BlogPost(models.Model):
    id = models.IntegerField(default=0, primary_key= True, editable=True, unique=True)
    userId = models.IntegerField(default=0)
    title = models.CharField(max_length= 100)
    body = models.CharField(max_length= 2000)

    def __str__(self):
        return self.title


