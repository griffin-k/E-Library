from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Book 
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User


from datetime import datetime


# Create your views here.
def libraian_dashboard(request):
    return render(request, "librarian_app/librarian_dashboard.html")


def add_member(request):
    return render(request, "librarian_app/add_member.html")


def add_book_form(request):
    return render(request, 'librarian_app/add_book.html') 





from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from datetime import datetime

def add_book(request):
    if request.method == 'POST':  
        print("✅ Received POST request")

        # Check if a file is uploaded
        if 'book_pdf' not in request.FILES:
            return JsonResponse({'success': False, 'error': 'No file uploaded'}, status=400)

        print("✅ PDF File received:", request.FILES['book_pdf'].name)

        # Fetch the last book entry using ID instead of accession_number
        last_book = Book.objects.order_by('-id').first()
        new_acc_no = f"ACC{last_book.id + 1}" if last_book else "ACC1"  # If no books, start from ACC1

        # Extract form data
        title = request.POST.get('book_title')
        category = request.POST.get('category')
        author = request.POST.get('author')
        publish_date = request.POST.get('published_date')
        edition = request.POST.get('edition')
        pdf_file = request.FILES['book_pdf']

        # Validate required fields
        if not all([title, category, author, publish_date, edition]):
            return JsonResponse({'success': False, 'error': 'All fields are required'}, status=400)

        # Convert publish_date
        try:
            publish_date = datetime.strptime(publish_date, "%Y-%m-%d").date()
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

        # Save book with the new accession number
        book = Book.objects.create(
            accession_number=new_acc_no,
            title=title,
            category=category,
            author=author,
            publish_date=publish_date,
            edition=edition,
            pdf_file=pdf_file
        )

        return JsonResponse({
            'success': True, 
            'message': 'Book added successfully', 
            'book_id': book.id, 
            'accession_number': new_acc_no
        })

    # ✅ Always calculate `new_acc_no` when rendering the form
    last_book = Book.objects.order_by('-id').first()
    new_acc_no = f"ACC{last_book.id + 1}" if last_book else "ACC1"

    print(f"📝 Accession Number Sent to Template: {new_acc_no}")  # Debugging Log

    return render(request, 'librarian_app/add_book.html', {'new_acc_no': new_acc_no})






from django.http import JsonResponse
from .models import Book

def get_next_accession_number(request):
    """Returns the next available accession number as JSON"""
    last_book = Book.objects.order_by('-id').first()
    if last_book:
        last_acc_no = int(last_book.accession_number.replace("ACC", ""))
        new_acc_no = f"ACC{last_acc_no + 1}"
    else:
        new_acc_no = "ACC100001"

    return JsonResponse({'new_acc_no': new_acc_no})




from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def show_books(request):
    query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    page_number = request.GET.get('page', 1)

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query) | books.filter(accession_number__icontains=query)

    if category_filter:
        books = books.filter(category=category_filter)

    # Pagination - Show 10 books per page
    paginator = Paginator(books, 10)
    page_obj = paginator.get_page(page_number)

    categories = Book.objects.values_list('category', flat=True).distinct()

    return render(request, 'librarian_app/show_books.html', {
        'books': page_obj,
        'categories': categories,
        'search_query': query,
        'selected_category': category_filter,
    })






from django.shortcuts import render
from auth_app.models import Student, Faculty, Staff

def show_members(request):
    search_query = request.GET.get("search", "")
    member_type = request.GET.get("type", "")

    # Fetch all members and add a type field
    students = Student.objects.select_related("user").all()
    faculty = Faculty.objects.select_related("user").all()
    staff = Staff.objects.select_related("user").all()

    members = [
        {"id": student.student_id, "name": f"{student.user.first_name} {student.user.last_name}", 
         "email": student.user.email, "cell_no": student.cell_no, "department": student.department, "type": "Student"}
        for student in students
    ] + [
        {"id": faculty_member.teacher_id, "name": f"{faculty_member.user.first_name} {faculty_member.user.last_name}", 
         "email": faculty_member.user.email, "cell_no": faculty_member.cell_no, "department": faculty_member.department, "type": "Faculty"}
        for faculty_member in faculty
    ] + [
        {"id": staff_member.staff_id, "name": f"{staff_member.user.first_name} {staff_member.user.last_name}", 
         "email": staff_member.user.email, "cell_no": "", "department": staff_member.department, "type": "Staff"}
        for staff_member in staff
    ]

    # Apply search filter
    if search_query:
        members = [m for m in members if search_query.lower() in m["name"].lower() or search_query in m["id"]]

    # Apply type filter
    if member_type and member_type != "All":
        members = [m for m in members if m["type"] == member_type]

    return render(request, "librarian_app/show_members.html", {
        "members": members,
        "search_query": search_query,
        "selected_type": member_type,
        "types": ["All", "Student", "Faculty", "Staff"]
    })

