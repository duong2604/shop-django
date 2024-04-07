from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)  # Harry Potter
    body = models.TextField()    # This the best novel which best sell on the world!....
    slug = models.SlugField()  # harry-potter
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null = True)
    image = models.ImageField(upload_to="images/", blank=True)
   
    
    