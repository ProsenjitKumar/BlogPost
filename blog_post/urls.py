from django.conf.urls import re_path
from .views import (
    PostList,
    DetailPost,
)

app_name = 'blog_post'


urlpatterns = [
    re_path(r'^$', PostList.as_view(), name='home'),
    re_path(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', DetailPost.as_view(), name='post_detail'),
]