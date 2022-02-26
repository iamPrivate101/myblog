from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,  #checks for login
    UserPassesTestMixin, #checks for valid user
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Post


# function base view
def home(request):
    context = {
        "posts": Post.objects.all(),
        "title": "Home",
    }
    return render(request, "blog/home.html", context)


# class based view for listing all blog post
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post
    # <app>/<model>_<viewtype>.html
    # this class automatically search for blog/post_detailview.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    # taking the logged user as author while creating post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # checking the blog author , and restrict other author from updating
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
    context = {
        "title": "About",
    }
    return render(request, "blog/about.html", context)
