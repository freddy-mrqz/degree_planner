from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from planner.models.course import Course

class CourseResource(resources.ModelResource):

  class Meta:
    model = Course
    import_id_fields = ('course_id',)
    exclude = ('id',)

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
  resource_class = CourseResource