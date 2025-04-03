from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, Faculty, Staff
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required






def login_view(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.POST.get('student_id') or request.POST.get('faculty_id') or request.POST.get('username')

        try:
            if user_type == 'student':
                user = Student.objects.get(student_id=user_id, email=email)
            elif user_type == 'faculty':
                user = Faculty.objects.get(faculty_id=user_id, email=email)
            elif user_type == 'staff':
                user = Staff.objects.get(staff_id=user_id, email=email)
            else:
                messages.error(request, "Invalid user type")
                return render(request, 'auth_app/login.html')

            if user.check_password(password):
  
                request.session['user_id'] = str(user.id)  
                request.session['user_type'] = user_type
                messages.success(request, f"Welcome, {user.first_name}")
                
                if user_type == 'staff':  # Admin
                    return redirect('librarian_dashboard')
                else:  # Student or Faculty
                    return redirect('student_page')
            else:
                messages.error(request, "Invalid password")
        except (Student.DoesNotExist, Faculty.DoesNotExist, Staff.DoesNotExist):
            messages.error(request, "Invalid ID or email")

    return render(request, 'auth_app/login.html')



 




def register(request):
    if request.method == "POST":
        try:
            user_type = request.POST.get('user_type')
            first_name = request.POST.get('first_name').capitalize()  
            last_name = request.POST.get('last_name').capitalize()   
            id_value = request.POST.get('id')
            cell_no = request.POST.get('cell_no')
            email = request.POST.get('email')
            department = request.POST.get('department')
            password = request.POST.get('password')
            if not all([first_name, last_name, id_value, cell_no, email, department, password]):
                messages.error(request, "All fields are required")
                return render(request, "auth_app/register.html")

            if user_type == "student":
                if Student.objects.filter(student_id=id_value).exists():
                    messages.error(request, "Student ID already exists")
                    return render(request, "auth_app/register.html")
                if Student.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return render(request, "auth_app/register.html")
                
                student = Student(
                    first_name=first_name,
                    last_name=last_name,
                    student_id=id_value,
                    cell_no=cell_no,
                    email=email,
                    department=department
                )
                student.set_password(password)
                student.save()
                messages.success(request, "Student registered successfully")
                return redirect('login')

            elif user_type == "faculty":
                if Faculty.objects.filter(faculty_id=id_value).exists():
                    messages.error(request, "Faculty ID already exists")
                    return render(request, "auth_app/register.html")
                if Faculty.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return render(request, "auth_app/register.html")
                
                faculty = Faculty(
                    first_name=first_name,
                    last_name=last_name,
                    faculty_id=id_value,
                    cell_no=cell_no,
                    email=email,
                    department=department
                )
                faculty.set_password(password)
                faculty.save()
                messages.success(request, "Faculty registered successfully")
                return redirect('login')

            elif user_type == "staff":
                if Staff.objects.filter(staff_id=id_value).exists():
                    messages.error(request, "Staff ID already exists")
                    return render(request, "auth_app/register.html")
                if Staff.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return render(request, "auth_app/register.html")
                
                staff = Staff(
                    first_name=first_name,
                    last_name=last_name,
                    staff_id=id_value,
                    cell_no=cell_no,
                    email=email,
                    department=department
                )
                staff.set_password(password)
                staff.save()
                messages.success(request, "Staff registered successfully")
                return redirect('login')

            else:
                messages.error(request, "Invalid user type")
                return render(request, "auth_app/register.html")

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, "auth_app/register.html")

    return render(request, "auth_app/register.html")



def logout_view(request):
    logout(request) 
    messages.success(request, "Logout successful!")
    return redirect("student_page") 


@login_required
def student_dashboard(request):
    return render(request, "dashboard/student_dashboard.html")

@login_required
def faculty_dashboard(request):
    return render(request, "auth_app/faculty_dashboard.html")

@login_required
def staff_dashboard(request):
    return render(request, "auth_app/staff_dashboard.html")