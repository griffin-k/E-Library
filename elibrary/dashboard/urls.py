from django.urls import path
from .views import student_page,newArivals

urlpatterns = [
    path("", student_page, name="student_page"),
    path("newarivals/", newArivals, name="newarivals"),
]
