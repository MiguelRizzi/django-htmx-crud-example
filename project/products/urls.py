from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("product_list/", views.ProductListView.as_view(), name="product_list"),
    path("product_create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
]
