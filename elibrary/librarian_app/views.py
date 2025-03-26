from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
import os
import csv

from .models import Book
from auth_app.models import Student, Faculty, Staff



from datetime import datetime


# Create your views here.
from auth_app.models import Student, Faculty  # Import Student & Faculty models

def librarian_dashboard(request):
    total_books = Book.objects.count()  # Count all books
    total_members = Student.objects.count()  # Count all students (members)
    total_faculty = Faculty.objects.count()  # Count all faculty members

    context = {
        "total_books": total_books,
        "total_members": total_members,
        "total_faculty": total_faculty,
    }
    return render(request, "librarian_app/librarian_dashboard.html", context)


def add_member(request):
    return render(request, "librarian_app/add_member.html")


def add_book_form(request):
    return render(request, 'librarian_app/add_book.html') 






def add_book(request):
    if request.method == 'POST':  

        if 'book_pdf' not in request.FILES:
            return JsonResponse({'success': False, 'error': 'No file uploaded'}, status=400)

        last_book = Book.objects.order_by('-id').first()
        new_acc_no = f"ACC{last_book.id + 1}" if last_book else "ACC1"  

        title = request.POST.get('book_title')
        category = request.POST.get('category')
        author = request.POST.get('author')
        publish_date = request.POST.get('published_date')
        edition = request.POST.get('edition')
        pdf_file = request.FILES['book_pdf']

        if not all([title, category, author, publish_date, edition]):
            return JsonResponse({'success': False, 'error': 'All fields are required'}, status=400)

        try:
            publish_date = datetime.strptime(publish_date, "%Y-%m-%d").date()
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

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

    last_book = Book.objects.order_by('-id').first()
    new_acc_no = f"ACC{last_book.id + 1}" if last_book else "ACC1"

    return render(request, 'librarian_app/add_book.html', {'new_acc_no': new_acc_no})


def get_next_accession_number(request):
    last_book = Book.objects.order_by('-id').first()
    if last_book:
        last_acc_no = int(last_book.accession_number.replace("ACC", ""))
        new_acc_no = f"ACC{last_acc_no + 1}"
    else:
        new_acc_no = "ACC100001"

    return JsonResponse({'new_acc_no': new_acc_no})



def show_books(request):
    query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    page_number = request.GET.get('page', 1)

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query) | books.filter(accession_number__icontains=query)

    if category_filter:
        books = books.filter(category=category_filter)

    paginator = Paginator(books, 10)
    page_obj = paginator.get_page(page_number)

    categories = Book.objects.values_list('category', flat=True).distinct()

    return render(request, 'librarian_app/show_books.html', {
        'books': page_obj,
        'categories': categories,
        'search_query': query,
        'selected_category': category_filter,
    })



def show_members(request):
    search_query = request.GET.get("search", "")
    member_type = request.GET.get("type", "")


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


    if search_query:
        members = [m for m in members if search_query.lower() in m["name"].lower() or search_query in m["id"]]


    if member_type and member_type != "All":
        members = [m for m in members if m["type"] == member_type]

    return render(request, "librarian_app/show_members.html", {
        "members": members,
        "search_query": search_query,
        "selected_type": member_type,
        "types": ["All", "Student", "Faculty", "Staff"]
    })





def settings_page(request):
    return render(request, "librarian_app/settings.html")


def download_members_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="members.csv"'
    
    writer = csv.writer(response)
    writer.writerow(["ID", "Name", "Email", "Cell No", "Department", "Type"])

    students = Student.objects.select_related("user").all()
    faculty = Faculty.objects.select_related("user").all()
    staff = Staff.objects.select_related("user").all()

    for student in students:
        writer.writerow([student.student_id, f"{student.user.first_name} {student.user.last_name}", student.user.email, student.cell_no, student.department, "Student"])
    
    for faculty_member in faculty:
        writer.writerow([faculty_member.teacher_id, f"{faculty_member.user.first_name} {faculty_member.user.last_name}", faculty_member.user.email, faculty_member.cell_no, faculty_member.department, "Faculty"])
    
    for staff_member in staff:
        writer.writerow([staff_member.staff_id, f"{staff_member.user.first_name} {staff_member.user.last_name}", staff_member.user.email, "", staff_member.department, "Staff"])

    return response


def download_books_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(["Accession Number", "Title", "Author", "Category", "Edition", "Published Date"])

    books = Book.objects.all()
    for book in books:
        writer.writerow([book.accession_number, book.title, book.author, book.category, book.edition, book.publish_date])

    return response





def support_desk(request):
    return render(request, 'librarian_app/support_desk.html')

def support_submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        print(f"Support request from {name} ({email}): {message}")

        messages.success(request, "Your support request has been submitted successfully!")
        return redirect('support_desk')

    return redirect('support_desk')




    