from django.views.generic import ListView, DetailView
from .models import BlogPost


class PostList(ListView):
    model = BlogPost
    template_name = 'blog_post/post_list.html'



class DetailPost(DetailView):
    model = BlogPost
    template_name = 'blog_post/post_detail.html'




