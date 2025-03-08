from django.shortcuts import render

# Create your views here.
def libraian_dashboard(request):
    return render(request, "librarian_app/librarian_dashboard.html")


def add_member(request):
    return render(request, "librarian_app/add_member.html")