from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView

class CategoryListView(ListView):
    model = Category
    template_name = "main.html"
    context_object_name = "categories"
    def get_queryset(self):
        name_avto = Category.objects.filter(is_avto=True)
        return name_avto



class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

# class mainView(TemplateView):
#     template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if self.request.method == "POST":
    #         name = self.request.POST.get("name")
    #         phone = self.request.POST.get("phone")
    #         message = self.request.POST.get("message")
    #         return HttpResponse(
    #             f"{name}, Ваш номер '{phone}' и сообщение '{message}' удачно отправлены!"
    #         )
    #     return context_data


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, Ваш номер '{phone}' и сообщение '{message}' удачно отправлены!"
        )
    return render(request, "contacts.html")


# def avto_list(request):
#     categori_1 = Category.objects.get(id=1)
#     products_avto = Product.objects.filter(category=categori_1)
#     context = {
#         "products_avto": products_avto

    # }
    # return render(request, "avto_list.html", context)

# def moto_list(request):
#     categori_2 = Category.objects.get(id=2)
#     products_moto = Product.objects.filter(category=categori_2)
#     context = {
#         "products_moto": products_moto
#
#     }
#     return render(request, "moto_list.html", context)

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)