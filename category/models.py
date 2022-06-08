from django.urls import reverse
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.category_name}"
    
    def get_url(self):
        return reverse("programs_by_category", args = [self.slug])

                            # -------------Portofolio-------------#

class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    date = models.DateField(null= True)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = "images/portfolio")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse("programs_detail", args = [self.category.slug, self.slug])

    def __str__(self):
        return f"{self.title}"