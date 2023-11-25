from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, categories, product_detail

# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/product/', product_detail, name='product_detail'),
]