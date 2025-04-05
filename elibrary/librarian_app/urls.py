from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from librarian_app.views import (
    search_members, librarian_dashboard, add_member, add_book, add_book_form,
    get_next_accession_number, show_books, show_members, download_members_csv,
    download_books_csv, settings_page, support_desk, support_submit,fetch_books,
    fetch_book_categories,fetch_students_by_department,add_books_from_pdfs
)

app_name = 'librarian_app'  

urlpatterns = [
    path("auth/", include("auth_app.urls")),
    path("librarian_dashboard/", librarian_dashboard, name="librarian_dashboard"),
    path("add_member/", add_member, name="add_member"),
    path('addBook_form/', add_book_form, name='addBook_form'),  # Render Add Book page
    path('add_book/', add_book, name='add_book'),  
    path('get_next_accession_number/', get_next_accession_number, name='get_next_accession_number'),

    path("setting/", settings_page, name="setting"),
    path("download_members_csv/", download_members_csv, name="download_members_csv"),
    path("download_books_csv/", download_books_csv, name="download_books_csv"),

    path('show_books/', show_books, name='show_books'),



    # Consolidate show_members to one path
    path('members/', show_members, name='show_members'),  # Use this as the main path
    path('search-members/', search_members, name='search_members'),

    path('support/', support_desk, name='support_desk'),
    path('support/submit/', support_submit, name='support_submit'),







    ###API 
    path('fetch_books/', fetch_books, name='fetch_books'),
      path('fetch_book_categories/', fetch_book_categories, name='fetch_book_categories'),
    path('fetch_students_by_department/', fetch_students_by_department, name='fetch_students_by_department'),




    path('add-books/', add_books_from_pdfs, name='add_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)