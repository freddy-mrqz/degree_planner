from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from planner.models.course import Course
from planner.models.student import Student

class CourseResource(resources.ModelResource):

  class Meta:
    model = Course
    import_id_fields = ('course_id',)
    exclude = ('id',)

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
  resource_class = CourseResource

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)