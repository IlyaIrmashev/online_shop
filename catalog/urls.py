from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, CategoriesListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView


# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты

app_name = CatalogConfig.name
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]


