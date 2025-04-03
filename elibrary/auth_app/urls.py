from django.urls import path
from .views import login_view, logout_view, register, student_dashboard, faculty_dashboard, staff_dashboard
from django.urls import include
from librarian_app.views import librarian_dashboard



urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('register/', register, name='register'),
    path('librarian_dashboard/',librarian_dashboard , name='librarian_dashboard'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),




    
]



