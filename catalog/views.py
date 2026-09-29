from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category


def base(request):
    return render(request, "base.html")



def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваш номер '{phone}' и сообщение '{message}' удачно отправлены!"
        )
    return render(request, "contacts.html")


def avto_detail(request):
    categori_1 = Category.objects.get(id=1)
    products_avto = Product.objects.filter(category=categori_1)
    context = {
        "products_avto": products_avto

    }
    return render(request, "avto_detail.html", context)

def moto_detail(request):
    categori_2 = Category.objects.get(id=2)
    products_moto = Product.objects.filter(category=categori_2)
    context = {
        "products_moto": products_moto

    }
    return render(request, "moto_detail.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)