from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, categories, catalog_product

# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/catalog/', catalog_product, name='catalog_product'),
]