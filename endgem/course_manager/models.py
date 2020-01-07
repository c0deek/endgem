from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=7, unique=True)
	name = models.CharField(max_length=128, unique=True)
	downloads = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Course, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Document(models.Model):

	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	file = models.FileField()
	downloads = models.IntegerField(default=0)

	def __str__(self):
		return self.title