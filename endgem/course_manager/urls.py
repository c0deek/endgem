from django.urls import path
from . import views

app_name = 'course_manager'

urlpatterns = [
	path('', views.index, name="index"),
	path('courses/', views.show_courses, name="show_courses"),
	path('<str:title>/download/', views.download_file, name="download_file"),
	path('add_course/', views.add_course, name="add_course"),
	path('<slug:course_code_slug>/', views.show_documents, name='show_course'),
	path('course/<slug:course_code_slug>/add_file/', views.add_document, name="add_file"),
]