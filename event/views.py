from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Join

# Create your views here.
def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request, 'event/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'event/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['date_time']
    paginate_by = 3 

class UserEventListView(ListView):
    model = Join
    template_name = 'event/join_list.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    paginate_by = 3 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Join.objects.filter(username=user)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'date_time', 'location', 'max_participants', 'content','banner']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'date_time', 'location', 'max_participants', 'content','banner']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'event/about.html', {'title': 'About'})



class JoinEventView(LoginRequiredMixin, CreateView):
    model = Join
    fields = ['title', 'name', 'email', 'phone', 'place']
    template_name = 'event/join_form.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
