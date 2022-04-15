from django.shortcuts import render
from .models import aboutme,skills,recomendation
from category.models import Category
# Create your views here.
def index(request):
    about = aboutme.objects.all()
    skill = skills.objects.all()
    recomendations = recomendation.objects.all()
    return render(request, "resumeapp/index.html", {
        "about":about,
        "skills":skill,
        "recomendationss":recomendations
    })

