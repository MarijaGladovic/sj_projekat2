from django.shortcuts import render
from .models import Post
from django.views.generic import (
    
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

context={}


def home(request):
	posts = Post.objects.order_by('-date_posted')
	context['posts'] = posts
	return render (request, 'blog/home.html', context)


class PostDetailView(DetailView):
	model=Post 

	#blog/post_detail.html
	#<app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
	model=Post 
	fields=['title','content']

	def form_valid(self, form): 
		form.instance.author=self.request.user
		#post.author=request.user #neka bude tako
		return super().form_valid(form)
		#super se samopoziva

	#blog/post_form.html - vazi i za update


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,):
	model=Post 
	fields=['title','content']

	def form_valid(self, form): 
		form.instance.author=self.request.user
		return super().form_valid(form)

	#UserPassesTestMixin - proverava da li je author isti kao i ovaj ulogovan
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
			messages.success(request, f'Updated successfuly.')
		messages.error(request, f'You are not post author. Cannot update.')
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url='/'#da zna gde da ode kada obrise post
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		messages.error(request, f'You are not post author. Cannot delete.')

	#post_confirm_delete.html
		return False