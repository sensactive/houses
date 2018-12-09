from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from os import path

_MAX_SIZE = 300
# Create your models here.
class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars/%Y/%m/%d', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True, blank=True)
        # Функция ограничения размера аватарки
    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(ShopUser, self).save(*args, **kwargs)

        # Проверяем, указан ли аватар
        if self.avatar:
            filename = self.avatar.path
            width = self.avatar.width
            height = self.avatar.height

            max_size = max(width, height)

            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filename)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
                image.save(filename)