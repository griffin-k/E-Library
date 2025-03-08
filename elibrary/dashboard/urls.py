from django.urls import path
from .views import student_page

urlpatterns = [
    path("students/", student_page, name="student_page"),
]
