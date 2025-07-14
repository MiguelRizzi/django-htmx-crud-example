from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm

import json


class IndexView(View):
    def get(self, request):
        return render(request, 'products/index.html')


class ProductListView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        products = Product.objects.all()
        if query:
            products = products.filter(name__icontains=query)
        return render(request, 'products/product_list.html', {'products': products})
    

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=201,
                headers={
                    'HX-Trigger': json.dumps({
                        "refreshProducts": None,
                    })
                }
            )
        return render(request, 'products/product_form.html', {'form': form})
    

class ProductUpdateView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'products/product_form.html', {'form': form})
    
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=200,
                headers={
                    'HX-Trigger': json.dumps({
                        'refreshProducts': None,
                    })
                }
            )
        return render(request, 'products/product_form.html', {'form': form})

    
class ProductDeleteView(View):
    def delete(self, request, pk):
        products = Product.objects.get(pk=pk)
        products.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    'refreshProducts': None,
                })
            }
        )
    
    