from django.urls import path
from . import views

app_name = 'course_manager'

urlpatterns = [
	path('', views.index, name="index"),
	path('category/<slug:course_code_slug>/', views.show_course, name='show_course'),
	path('add_category/', views.add_course, name="add_course"),
	path('category/<slug:course_code_slug>/add_file/', views.add_file, name="add_file"),
]