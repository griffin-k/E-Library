from django.urls import path
from .views import login_view, register, student_dashboard, faculty_dashboard, staff_dashboard
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", login_view, name="login"),
    path('register/', register, name='register'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    
]



