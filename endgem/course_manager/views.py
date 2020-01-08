from django.shortcuts import render, redirect
from .models import Course, Document
from .forms import CourseForm, DocumentForm
from django.http import HttpResponse

# Create your views here.
def index(request):
	course_list = Course.objects.order_by('-downloads')[:5]
	document_list = Document.objects.order_by('-downloads')[:5]

	context = { 'courses': course_list, 'documents': document_list }

	return render (request, 'course_manager/index.html', context=context)

def show_courses(request):
	context = {}
	try:
		course = Course.objects.all()
		context['courses'] = course
	except Course.DoesNotExist:
		context['courses'] = None
		
	return render (request, 'course_manager/courses.html', context=context)

def show_documents(request, course_code_slug):
	context = {}
	try:
		course = Course.objects.get(slug=course_code_slug)
		document = Document.objects.filter(course=course)
		context['documents'] = document
		context['course'] = course
	except Course.DoesNotExist:
		context['documents'] = None
		context['course'] = None

	return render (request, 'course_manager/documents.html', context=context)

def add_course(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

	else:
		form = CourseForm()

	return render(request, 'course_manager/add_course.html', {'form': form})

def add_document(request, course_code_slug):
	try:
		course = Course.objects.get(slug=course_code_slug)
	except Course.DoesNotExist:
		course = None

	form = DocumentForm()
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			if course:
				document = form.save(commit = False)
				document.course = course
				document.save()
				return redirect(f'course/{course_code_slug}')
			else:
				# print(form.errors)
				pass

	context_dic = {'form': form, 'course': course}
	return render(request, 'course_manager/add_document.html', context_dic)


def download_file(request, title):
	# course = Course.objects.get(slug=course_slug)
	document = Document.objects.get(title=title)
	course = document.course
	print(course.code)
	if document:
		# if 'downloaded' in request.COOKIES.keys():
			doc_downloads = document.downloads + 1
			document.downloads = doc_downloads
			corse_downloads = course.downloads + 1
			course.downloads = corse_downloads
			document.save()
			course.save()
		# else:
			# response.set_cookie('downloaded', 1)
			# return response
	return redirect(f"/media/{ document.file }/")