from django.shortcuts import render
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all().values()
    return render(request, 'homepage.html', {
        'posts': posts
    })


# def detailed_Post(request, id):
#     data =  Post.objects.all()[id]
#     return render(request, "detailed_post.html", {"post": data})