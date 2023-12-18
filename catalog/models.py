from django.conf import settings
from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    picture = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_last_modified = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name='Создал')
    is_published = models.BooleanField(default=True, verbose_name='статус публикации')

    #anonymous_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='анонимный пользователь')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.CharField(max_length=20, verbose_name='номер версии')
    name_version = models.CharField(max_length=250, verbose_name='название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.name_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='контакты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)
