from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source="teacher_id.name")

    class Meta:
        model = Student
        fields = ('name', 'teacher')


class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(source="student_set", many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ('name', 'students')

    
    