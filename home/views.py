from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, "login.html")

def registration(request):
    if request.method == "POST":
        email = request.POST["input_email"]
        password = request.POST["input_password"]
        username = request.POST["input_username"]
        age = request.POST["input_age"]
    return render(request, "registration.html")