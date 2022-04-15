from distutils.command.upload import upload
from django.db import models

# Create your models here.

class aboutme(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField()
    number = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "images")
    description = models.TextField(max_length=500)


    class Meta:
        verbose_name = 'aboutme'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class skills(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "images/skills")

    class Meta:
        verbose_name = 'skills'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name}"

class recomendation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    recomendation = models.TextField(max_length=500)
    image = models.ImageField(upload_to = "images/recomendators")
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
