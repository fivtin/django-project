from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.


def main_page(request):
    context = {
        'objects': Product.objects.all()
    }
    return render(request, "catalog/main.html", context)


def product_detail(request, pk: int):
    context = {
        'object': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    if request.POST:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"name: {name}, email: {phone}, message: {message}")
    return render(request, "catalog/contacts.html")
