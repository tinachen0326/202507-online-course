from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('enrollments/', views.enroll_student, name='enroll-student'),
]
