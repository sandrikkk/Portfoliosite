from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/blog")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True, null = True, max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(5000)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null = True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    dated_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)