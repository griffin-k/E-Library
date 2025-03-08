from django.urls import path
from .views import student_page,newArivals,byCategory

urlpatterns = [
    path("", student_page, name="student_page"),
    path("newarivals/", newArivals, name="newarivals"),
    path("bycategory/", byCategory, name="bycategory"),
]
