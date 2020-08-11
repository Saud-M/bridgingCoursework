from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.

class PersonalProfile(models.Model):
	personal_profile = models.TextField(default='')


class Course(models.Model):
	
	course = models.CharField(max_length=60, default='')
	def __str__(self):
		return f'{self.course}'

class Education(models.Model):
	title = models.CharField(max_length=120)
	details = models.TextField(default='', blank=True)
	courses = models.ManyToManyField(Course, blank=True)

	def __str__(self):
		return f'{self.title}'

	
class ProficientProgrammingLanguage(models.Model):
	ppl = models.CharField(max_length=30)
	def __str__(self):
		return f'{self.ppl}'

class FamiliarProgrammingLanguage(models.Model):
	fpl = models.CharField(max_length=30)
	def __str__(self):
		return f'{self.fpl}'

class Language(models.Model):
	language = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.language}'