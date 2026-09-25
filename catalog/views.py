from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваш номер '{phone}' и сообщение '{message}' удачно отправлены!"
        )
    return render(request, "contacts.html")

def base(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "base.html", context)

