from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .filters import ProductFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import *
from django import forms


class PostList(ListView):
    model = Post
    ordering = '-time_created'
    template_name = 'news.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news_pk.html'
    context_object_name = 'post'

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news')
    form = PostForm()
    return render(request, 'post_create.html', {'form': form})

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'NE'
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.post_type = 'AR'
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'







