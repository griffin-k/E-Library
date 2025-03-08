from django.contrib import admin
from django.urls import path, include
from dashboard.views import student_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth_app.urls")), 
    path("dashboard/", include("dashboard.urls")),
    path("librarian/", include("librarian_app.urls")),

    path("", student_page, name="student_page"),
]
