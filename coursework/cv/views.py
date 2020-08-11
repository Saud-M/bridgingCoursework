from django.shortcuts import render
from cv.models import PersonalProfile, Education, ProficientProgrammingLanguage, FamiliarProgrammingLanguage, Language, Course

# Create your views here.

def cv(request, *args, **kwargs):

    profiles = PersonalProfile.objects.all()
    educations = Education.objects.all()
    proficientLanguages = ProficientProgrammingLanguage.objects.all()
    familiarLanguages = FamiliarProgrammingLanguage.objects.all()
    languages = Language.objects.all()
    courses = Course.objects.all()


    context = {'profiles': profiles,
                'educations': educations,
                'proficientLanguages':proficientLanguages,
                'familiarLanguages': familiarLanguages,
                'languages':languages,
                'courses': courses }

    return render(request, 'cv/cv.html', context)