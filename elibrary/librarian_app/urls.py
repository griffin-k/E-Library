from django.contrib import admin
from django.urls import path, include
from librarian_app.views import libraian_dashboard, add_member

urlpatterns = [

    path("libraian_dashboard/", libraian_dashboard, name="libraian_dashboard"),
    path("add_member/", add_member, name="add_member"),
]
