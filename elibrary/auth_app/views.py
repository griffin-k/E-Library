from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, Faculty
import re
from django.contrib.auth import login 
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Student, Faculty, Staff



def login_view(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        email = request.POST.get("email")
        password = request.POST.get("password")
        student_id = request.POST.get("student_id", None)
        faculty_id = request.POST.get("faculty_id", None)
        staff_id = request.POST.get("staff_id", None)

        try:
            user = None

            if user_type == "student":
                student = Student.objects.get(student_id=student_id)
                user = student.user
            elif user_type == "faculty":
                faculty = Faculty.objects.get(teacher_id=faculty_id)
                user = faculty.user
            elif user_type == "staff":
                staff = Staff.objects.get(staff_id=staff_id)
                user = staff.user
            else:
                messages.error(request, "Invalid user type.")
                return redirect("login")

            if user and check_password(password, user.password):
                login(request, user)
                request.session["user_id"] = user.id
                request.session["user_type"] = user_type
                messages.success(request, "Login successful!")

                if user_type == "student":
                    return redirect("student_dashboard")
                elif user_type == "faculty":
                    return redirect("faculty_dashboard")
                elif user_type == "staff":
                    return redirect("staff_dashboard")

            else:
                messages.error(request, "Invalid credentials.")
                return redirect("login")

        except (Student.DoesNotExist, Faculty.DoesNotExist, Staff.DoesNotExist, User.DoesNotExist):
            messages.error(request, "User not found.")
        except User.MultipleObjectsReturned:
            messages.error(request, "Multiple accounts found. Contact admin.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, "auth_app/login.html")



def register(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        first_name = request.POST.get("first_name").strip()
        last_name = request.POST.get("last_name").strip()
        email = request.POST.get("email").strip()
        cell_no = request.POST.get("cell_no").strip()
        dept = request.POST.get("dept")
        password = request.POST.get("password")
        
        # Validation
        if not first_name or not last_name:
            messages.error(request, "First Name and Last Name are required.")
            return redirect("register")

        if not re.match(r'^[a-zA-Z]+$', first_name) or not re.match(r'^[a-zA-Z]+$', last_name):
            messages.error(request, "First Name and Last Name should contain only alphabets.")
            return redirect("register")

        if not re.match(r'^\+?\d{10,15}$', cell_no):
            messages.error(request, "Invalid phone number format.")
            return redirect("register")

        if not email.endswith("@gmail.com"):
            messages.error(request, "Email must end with @gmail.com")
            return redirect("register")

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return redirect("register")

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)

        if user_type == "student":
            student_id = request.POST.get("student_id").strip()
            if not student_id:
                messages.error(request, "Student ID is required.")
                return redirect("register")

            Student.objects.create(user=user, student_id=student_id, cell_no=cell_no, department=dept)
            messages.success(request, "Student registered successfully!")

        elif user_type == "faculty":
            teacher_id = request.POST.get("teacher_id").strip()
            if not teacher_id:
                messages.error(request, "Teacher ID is required.")
                return redirect("register")

            Faculty.objects.create(user=user, teacher_id=teacher_id, cell_no=cell_no, department=dept)
            messages.success(request, "Faculty registered successfully!")

        return redirect("login") 

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