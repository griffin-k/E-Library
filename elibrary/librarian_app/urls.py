from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from librarian_app.views import libraian_dashboard, add_member,add_book, add_book_form,get_next_accession_number,show_books,show_members, download_members_csv, download_books_csv,settings_page,support_desk,support_submit

urlpatterns = [

    path("libraian_dashboard/", libraian_dashboard, name="libraian_dashboard"),
    path("add_member/", add_member, name="add_member"),
    path('addBook_form/', add_book_form, name='addBook_form'),  # Render Add Book page
    path('add_book/', add_book, name='add_book'),  
    path('get_next_accession_number/', get_next_accession_number, name='get_next_accession_number'),
    path('show_books/', show_books, name='show_books'),
    path("members/", show_members, name="show_members"),
    path("setting/", settings_page, name="setting"),
    path("download_members_csv/", download_members_csv, name="download_members_csv"),
    path("download_books_csv/", download_books_csv, name="download_books_csv"),



    path('support/', support_desk, name='support_desk'),
    path('support/submit/',support_submit, name='support_submit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)