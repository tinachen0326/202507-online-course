from django.contrib import admin
from .models import Teacher, Student, Course, Enrollment
from .import models

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'level')
    search_fields = ('name', 'email')
    list_filter = ('level',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'get_teachers')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'teachers')
    filter_horizontal = ('teachers',)
    
    def get_teachers(self, obj):
        return ", ".join([teacher.name for teacher in obj.teachers.all()])
    get_teachers.short_description = '授課老師'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__name', 'course__title')
    list_filter = ('enrolled_at', 'course')
    readonly_fields = ('enrolled_at',)

