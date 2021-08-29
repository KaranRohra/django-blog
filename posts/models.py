from django.db import models
from django.utils import text


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "posts_categories"


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(default="", editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        return self.super(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts_posts"
