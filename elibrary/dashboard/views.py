from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse
from librarian_app.models import Book
from auth_app.models import Student, Faculty, Staff
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
import os
from django.shortcuts import get_object_or_404
from django.conf import settings




def student_page(request):
    user = None
    user_id = request.session.get('user_id')
    user_type = request.session.get('user_type')

    if user_id and user_type:
        try:
            if user_type == 'student':
                user = Student.objects.get(id=user_id)
            elif user_type == 'faculty':
                user = Faculty.objects.get(id=user_id)
            elif user_type == 'staff':
                user = Staff.objects.get(id=user_id)
        except (Student.DoesNotExist, Faculty.DoesNotExist, Staff.DoesNotExist):
            pass  

    return render(request, "dashboard/student_dashboard.html", {'user': user})

def newArivals(request):
    return render(request, "dashboard/newArivals.html")


def browse_books(request):
    search_query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')

    books = Book.objects.all()

    if search_query:
        books = books.filter(title__icontains=search_query) | books.filter(author__icontains=search_query)

    if selected_category:
        books = books.filter(category=selected_category)


    paginator = Paginator(books, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Book.objects.values_list('category', flat=True).distinct()

    return render(request, 'dashboard/browse_books.html', {
        'books': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'MEDIA_URL': settings.MEDIA_URL,  
    })



def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    file_path = book.pdf_file.path
    if not os.path.exists(file_path):
        raise Http404("The requested book file does not exist")
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
        return response