from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import student_page, newArivals, browse_books,download_book,about,profile_view,book_cover1,book_cover2,book_cover3
from auth_app.views import logout_view

urlpatterns = [
    path("", student_page, name="student_page"),
    path("newarivals/", newArivals, name="newarivals"),
    path('browse_books/', browse_books, name='browse_books'),
    path('logout/', logout_view, name="logout"),
    path('aboutus/', about, name='aboutus'),
    path('profile/', profile_view, name='profile'), 
    path('download_book/<int:book_id>/', download_book, name='download_book'),
    path('book_cover1/', book_cover1, name='book_cover1'),
    path('book_cover2/', book_cover2, name='book_cover2'),
    path('book_cover3/', book_cover3, name='book_cover3'),
    




] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)