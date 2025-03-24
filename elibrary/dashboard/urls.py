from django.urls import path
from .views import student_page,newArivals,browse_books,download_book
from auth_app.views import logout_view

urlpatterns = [
    path("", student_page, name="student_page"),
    path("newarivals/", newArivals, name="newarivals"),
    path('browse_books/', browse_books, name='browse_books'),
    path('download/<int:book_id>/', download_book, name='download_book'),
    path('logout_view/', logout_view, name="logout_view"),

]
