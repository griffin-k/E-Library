from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User


def login_view(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        email = request.POST.get("email")
        password = request.POST.get("password")
        student_id = request.POST.get("student_id", None)
        faculty_id = request.POST.get("faculty_id", None)
        username = request.POST.get("username", None)

        try:
            # Identify user based on their type
            if user_type == "student":
                user = User.objects.get(student_id=student_id, email=email, user_type="student")
            elif user_type == "faculty":
                user = User.objects.get(teacher_id=faculty_id, email=email, user_type="faculty")
            elif user_type == "staff":
                user = User.objects.get(username=username, email=email, user_type="staff")
            else:
                messages.error(request, "Invalid user type.")
                return redirect("login")

            # Verify Password
            if check_password(password, user.password):
                request.session["user_id"] = user.id
                request.session["user_type"] = user.user_type
                messages.success(request, "Login successful!")
                return redirect("student_page")  # Redirect to dashboard
            else:
                messages.error(request, "Invalid credentials.")
                return redirect("login")

        except User.DoesNotExist:
            messages.error(request, "User not found.")
        except User.MultipleObjectsReturned:
            messages.error(request, "Multiple accounts found. Contact admin.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, "auth_app/login.html")


def register_view(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("cell_no")
        department = request.POST.get("dept")
        password = request.POST.get("password")
        hashed_password = make_password(password)  # Securely hash password

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        # Create Student User
        if user_type == "student":
            student_id = request.POST.get("student_id")

            if User.objects.filter(student_id=student_id).exists():
                messages.error(request, "Student ID already registered.")
                return redirect("register")

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                department=department,
                user_type="student",
                student_id=student_id,
                password=hashed_password,
            )

        # Create Faculty User
        elif user_type == "faculty":
            teacher_id = request.POST.get("teacher_id")

            if User.objects.filter(teacher_id=teacher_id).exists():
                messages.error(request, "Faculty ID already registered.")
                return redirect("register")

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                department=department,
                user_type="faculty",
                teacher_id=teacher_id,
                password=hashed_password,
            )

        else:
            messages.error(request, "Invalid user type.")
            return redirect("register")

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "auth_app/register.html")
