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
	title = forms.CharField(max_length=128, help_text='Document name')
	file = forms.URLField(max_length=200, help_text='Please enter the URL of the document.')
	downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Document
		exclude = ('downloads',)