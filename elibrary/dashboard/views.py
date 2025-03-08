from django.shortcuts import render

def student_page(request):
    return render(request, "dashboard/student.html")



def newArivals(request):
    return render(request, "dashboard/newArivals.html")