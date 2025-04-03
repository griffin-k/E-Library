from django.contrib import admin
from django.urls import path, include
from dashboard.views import student_page
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth_app.urls")), 
    path("dashboard/", include("dashboard.urls")),
    path("librarian/", include("librarian_app.urls")),

    path("", student_page, name="student_page"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)