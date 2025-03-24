from django.shortcuts import render
from django.shortcuts import render
from django.http import FileResponse
from librarian_app.models import Book

from django.core.paginator import Paginator
from django.shortcuts import render

def student_page(request):
    return render(request, "dashboard/student_dashboard.html")

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
    })


def download_book(request, book_id):
    book = Book.objects.get(id=book_id) 
    response = FileResponse(book.pdf_file.open(), as_attachment=True, filename=book.pdf_file.name)
    return response
