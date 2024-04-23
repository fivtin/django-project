from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, "catalog/home.html")


def contacts_page(request):
    if request.POST:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"name: {name}, email: {phone}, message: {message}")
    return render(request, "catalog/contacts.html")
