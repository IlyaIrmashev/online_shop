from django.shortcuts import render

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


def home(request):
    context = {
        'object_list': Category.objects.all()[:4],
        'title': 'SkyStore'
    }
    return render(request, 'catalog/home.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'catalog/category.html', context)


def catalog_product(request, pk):
    catalog_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': f'Наши товары {catalog_item.name}'
    }
    return render(request, 'catalog/product.html', context)
