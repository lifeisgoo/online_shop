from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ProductModel


class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_queryset(self):
        return ProductModel.objects.all()
