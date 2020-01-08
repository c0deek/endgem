from django import forms
from .models import Course, Document

class CourseForm(forms.ModelForm):
	code = forms.CharField(max_length=7, help_text="e.g. MTN-101 (write in this format only)")
	name = forms.CharField(max_length=128, help_text="Course Name")
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
		fields = ('title', 'file')
		exclude = ('downloads',)