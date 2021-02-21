from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 