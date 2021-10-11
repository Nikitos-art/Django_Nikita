from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

class Index(TemplateView):
    template_name = 'mainapp/index.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['index'] = Index
    #     return context


class CategoriesListView(ListView):
    model = ProductCategory
    context_object_name = 'categories'
    template_name = 'mainapp/products.html'


class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/products.html'

    # def categorization(self, category_id=ProductCategory.pk):
    #     products = Product.objects.filter(category_id=category_id) if category_id != None else Product.objects.all()
    #
    #     context = {
    #         'title': 'Каталог',
    #         'categories': ProductCategory.objects.all(),
    #         'products': products
    #     }
    #     return render(self, 'mainapp/products.html', context)



# def dispatch(self, *args, **kwargs):
#     return super().dispatch(*args, **kwargs)


# def get_queryset(self):
#     return Product.objects.filter(category_id=self.request.user)


# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     return context

