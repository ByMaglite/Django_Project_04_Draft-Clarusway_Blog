from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    gs = Post.objects.all()
    context = {
        "objects_list":gs
    }
    return render(request,"blog/post_list.html", context)
