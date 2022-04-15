from django.db import models

# Create your models here.
class WorkExperienceCard(models.Model):
    workdate = models.CharField(max_length=20)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title}"

class EducationCard(models.Model):
    eddate = models.CharField(max_length=20)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.title}"

class LanguageSkills(models.Model):
    languagename = models.CharField(max_length=20)
    procent = models.IntegerField()

    class Meta:
        verbose_name = 'LanguageSkills'
        verbose_name_plural = 'Language Skills'

    def __str__(self):
        return f"{self.languagename}"

class CodingSkills(models.Model):
    title = models.CharField(max_length=30)
    procent = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'CodingSkills'
        verbose_name_plural = 'Coding Skills'
    def __str__(self):
        return f"{self.title}"