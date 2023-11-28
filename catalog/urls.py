from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, CategoriesListView

# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты

app_name = CatalogConfig.name
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product_detail'),
]
