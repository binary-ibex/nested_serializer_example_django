from classroom.models import Student, Teacher
from django.shortcuts import render
from rest_framework import generics
from .serializer import TeacherSerializer, StudentSerializer
# Create your views here.


class TeacherView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class StudentView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


