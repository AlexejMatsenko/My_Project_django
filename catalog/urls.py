from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, contacts, avto_detail, moto_detail, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", base, name="base"),
    path("contacts/", contacts, name="contacts"),
    path("avto_detail/", avto_detail, name="avto_detail"),
    path("moto_detail/", moto_detail, name="moto_detail"),
    path("products/<int:pk>/", product_detail, name="product_detail")
]
