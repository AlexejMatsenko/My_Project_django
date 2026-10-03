from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts,ProductDetailView
from catalog.views import ProductListView, CategoryListView
app_name = CatalogConfig.name

# urlpatterns = [
#     path("products/", ProductListView.as_view(), name="products_list"),
#     # path("contacts/", contacts, name="contacts"),
#     # path("avto_list/", avto_list, name="avto_list"),
#     # path("moto_list/", moto_list, name="moto_list"),
#     # path("products/<int:pk>/", product_detail, name="product_detail")
# ]

urlpatterns = [
    path("", CategoryListView.as_view(), name="main"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    # path("avtos/", CategoryListView.as_view(), name="avto_list"),
    # path("categories/", CategoryListView.as_view(), name="moto_list"),
    path("contacts/", contacts, name="contacts"),


    # path("products/<int:pk>/", product_detail, name="product_detail")
]
