from django.contrib import admin
from .models import EducationCard, WorkExperienceCard,LanguageSkills,CodingSkills
# Register your models here.
admin.site.register(EducationCard)
admin.site.register(WorkExperienceCard)
admin.site.register(LanguageSkills)
admin.site.register(CodingSkills)