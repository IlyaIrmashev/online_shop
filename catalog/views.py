from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Contacts, Product


# Create your views here.

# Контроллер == функция def_contacts()
#
def contacts(request):
    context = {
        'object_list': Contacts.objects.all(),
        'title': 'Наши контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


class HomeListView(ListView):
    model = Category
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Главная'}


class CategoriesListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {'title': 'Категории'}


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

