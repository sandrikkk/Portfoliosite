from django.shortcuts import render
from .models import EducationCard, WorkExperienceCard, LanguageSkills,CodingSkills
# Create your views here.
def resume(request):
    edcards = EducationCard.objects.all()
    workcards = WorkExperienceCard.objects.all()
    langskills = LanguageSkills.objects.all()
    codeskills = CodingSkills.objects.all()
    return render(request, "resumeapp/resume.html", {
        "edcards": edcards,
        "workcards": workcards,
        "langskills":langskills,
        "codeskills":codeskills
    })