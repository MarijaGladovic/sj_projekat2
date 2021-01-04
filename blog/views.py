from django.shortcuts import render
from .models import Post


context={}

def home(request):
	posts = Post.objects.order_by('-date_posted')
	context['posts'] = posts
	context['name'] = 'home'
	return render (request, 'blog/home.html', context)

