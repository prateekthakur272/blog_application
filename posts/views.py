from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts': posts})


def post(request, pk):
    selected_post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'selected_post': selected_post})
