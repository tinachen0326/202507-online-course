from django.db import models
from django.utils import timezone
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='老師姓名')
    email = models.EmailField(unique=True, verbose_name='電子信箱')
    bio = models.TextField(blank=True, verbose_name='老師介紹')

    class Meta:
        verbose_name = '老師'
        verbose_name_plural = '老師'
    
    def __str__(self):
        return self.name

class Student(models.Model):
    LEVEL_CHOICES = [
        ('初級', '初級'),
        ('中級', '中級'),
        ('高級', '高級'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='學生姓名')
    email = models.EmailField(unique=True, verbose_name='電子信箱')
    level = models.CharField(max_length=20, default='初級', choices=LEVEL_CHOICES, verbose_name='學生等級')

    class Meta:
        verbose_name = '學生'
        verbose_name_plural = '學生'
    
    def __str__(self):
        return f"{self.name} ({self.level})"

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='課程名稱')
    description = models.TextField(verbose_name='課程說明')
    teachers = models.ManyToManyField(Teacher, verbose_name='課程老師')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='建立時間')
    
    class Meta:
        verbose_name = '課程'
        verbose_name_plural = '課程'
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='學生')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='課程')
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name='報名時間')
    
    class Meta:
        unique_together = ('student', 'course')
        verbose_name = '報名記錄'
        verbose_name_plural = '報名記錄'
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
        
