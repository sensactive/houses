from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Категория')
    info = models.TextField(verbose_name='Описание категории')
    price = models.PositiveIntegerField(verbose_name='Цена от')
    img = models.ImageField(upload_to='categories/%Y/%m/%d', verbose_name='Картинка категории')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название проекта')
    info = models.TextField(verbose_name='Описание проекта')
    price = models.PositiveIntegerField(verbose_name='Цена')
    img = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Картинка проекта')
    category = models.ForeignKey(Category, on_delete=models.SET('NULL'), null=True)

    def __str__(self):
        return self.name