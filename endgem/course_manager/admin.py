from django.contrib import admin
from .models import Course, Document

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('code',)}

admin.site.register(Course, CourseAdmin)
admin.site.register(Document)

