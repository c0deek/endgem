from django import forms
from .models import Course, Document

class CourseForm(forms.ModelForm):
	code = forms.CharField(max_length=7, label="Course code(format: MTN-101)")
	name = forms.CharField(max_length=128, label="Course Name")
	downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Course
		exclude = ('downloads', 'slug')
		# fields = ('name',)

class DocumentForm(forms.ModelForm):
	# title = forms.CharField(max_length=128,)
	# downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	# file = forms.FileField(upload_to="../media/files")

	class Meta:
		model = Document
		fields = ('title', 'file',)
		# exclude = ('downloads',)