from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class LessonAdmin(admin.ModelAdmin):
    list_display = ["subject", "course"]


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    fieldsets = [
                 (None, {'fields': ["name", "short_description", "description", "coach", "assistant"]}),
                ]
    inlines = [LessonInline]
    search_fields = ["name"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
