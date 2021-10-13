from django.shortcuts import render
import os,json

from django.views.generic import TemplateView

from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

class Index(TemplateView):
    template_name = 'mainapp/index.html'


def products(request, category_id=None, page_id=1):
    # file_path = os.path.join(MODULE_DIR,'fixtures/goods.json')
    products = Product.objects.filter(category_id=category_id) if category_id != None else Product.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Катлог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }
    # context.update({'products':products_paginator})
    return render(request, 'mainapp/products.html', context)
