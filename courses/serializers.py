from rest_framework import serializers
from .models import Teacher, Student, Course, Enrollment

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    teacher_names = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_teacher_names(self, obj):
        return [teacher.name for teacher in obj.teachers.all()]

class CourseCreateSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Teacher.objects.all()
    )
    
    class Meta:
        model = Course
        fields = ['title', 'description', 'teachers']

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'student_name', 'course_title', 'enrolled_at']

class EnrollmentCreateSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    
    def validate(self, data):
        try:
            student = Student.objects.get(id=data['student_id'])
            course = Course.objects.get(id=data['course_id'])
        except Student.DoesNotExist:
            raise serializers.ValidationError("學生不存在")
        except Course.DoesNotExist:
            raise serializers.ValidationError("課程不存在")
        
        # 檢查是否已經報名
        if Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("學生已經報名此課程")
        
        return data
    
    def create(self, validated_data):
        student = Student.objects.get(id=validated_data['student_id'])
        course = Course.objects.get(id=validated_data['course_id'])
        return Enrollment.objects.create(student=student, course=course)
