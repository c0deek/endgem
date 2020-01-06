from django import forms
from rango.models import Course, Document

class CourseForm(forms.ModelForm):
	deptt = forms.Charfield()
	course-no = forms.IntegerField(max_length=3, help_text="Code")
	code = deptt + "-" + course-no
	name = forms.CharField(max_length=128, help_text="Course Name")
	downloads = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Course
		fields = ('name',)

class DocumentForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text='Please enter the title of the document.')
	url = forms.URLField(max_length=200, help_text='Please enter the URL of the document.')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Document
		# exclude = ('course',)