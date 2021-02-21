from classroom.views import TeacherView
from django.urls import path 
from .views import TeacherView, StudentView

urlpatterns = [ 
    path("teacher", TeacherView.as_view()),
    path("teacher/<int:pk>", TeacherView.as_view()),
    path("student", StudentView.as_view()),
    path("student/<int:pk>", StudentView.as_view()),
]