from django.db import models


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True)
    objects = EntryQuerySet.as_manager()


    def __str__(self):
        return self.title

