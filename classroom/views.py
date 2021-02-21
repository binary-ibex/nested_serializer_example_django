from classroom.models import Student, Teacher
from django.shortcuts import render
from rest_framework import generics
from .serializer import TeacherSerializer, StudentSerializer
# Create your views here.


class TeacherView(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        
        try:
            queryset = Teacher.objects.filter(id=self.kwargs['pk'])
        except:
            queryset = Teacher.objects.all()

        return queryset

class StudentView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        
        try:
            queryset = Student.objects.filter(id=self.kwargs['pk'])
        except:
            queryset = Student.objects.all()

        return queryset


