from django.contrib import admin

from .models import PersonalProfile, Education, ProficientProgrammingLanguage, FamiliarProgrammingLanguage, Language, Course
# Register your models here.
admin.site.register(PersonalProfile)
admin.site.register(Education)
admin.site.register(ProficientProgrammingLanguage)
admin.site.register(FamiliarProgrammingLanguage)
admin.site.register(Language)
admin.site.register(Course)