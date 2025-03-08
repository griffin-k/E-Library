from django.shortcuts import render

def student_page(request):
    return render(request, "dashboard/student.html")
