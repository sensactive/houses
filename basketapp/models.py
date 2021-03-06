from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

from mainapp.models import Product


# Create your models here.


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    @cached_property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    # !!!!!!!УВЕЛИЧИВАЕТ ЧИСЛО ДУБЛЕЙ, НО ТАКЖЕ РАБОЧИЙ ВАРИАНТ
    # @property
    # def total_quantity(self):
    #     "return total quantity for user"
    #     _items = Basket.objects.filter(user=self.user, product__is_active=True)
    #     _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
    #     return _totalquantity

    # @property
    # def total_cost(self):
    #     "return total cost for user"
    #     _items = Basket.objects.filter(user=self.user, product__is_active=True)
    #     _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
    #     return _totalcost

    # @staticmethod
    # def get_items(user):
    #     return Basket.objects.filter(user=user).order_by('product__category')

    # !!!!!!!! УМЕНЬШАЕТ ЧИСЛО ДУБЛЕЙ
    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    @cached_property
    def get_items(self):
        return self.user.basket.select_related()

    @property
    def total_quantity(self):
        _items = self.get_items
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        _items = self.get_items
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    @cached_property
    def get_summary(self):
        __items = self.get_items
        return {
            'total_quantity': sum(list(map(lambda x: x.quantity, __items))),
            'total_cost': sum(list(map(lambda x: x.product_cost, __items))),
        }

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()

# !!!!!!!!!!ТОЖЕ РАБОЧИЙ ВАРИАНТ КЕШИРОВАНИЯ, НО ОСТАВЛЯЕТ 4 ДУБЛЯ
# @cached_property
#     def product_cost(self):
#         "return cost of all products this type"
#         return self.product.price * self.quantity
#
#     @cached_property
#     def total_quantity(self):
#         "return total quantity for user"
#         _items = Basket.objects.filter(user=self.user, product__is_active=True).select_related('product', 'user')
#         _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
#         return _totalquantity
#
#     @cached_property
#     def total_cost(self):
#         "return total cost for user"
#         _items = Basket.objects.filter(user=self.user, product__is_active=True).select_related('product', 'user')
#         _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
#         return _totalcost
#
#     @staticmethod
#     def get_items(user):
#         return Basket.objects.filter(user=user).order_by('product__category')
#
#     @staticmethod
#     def get_item(pk):
#         return Basket.objects.filter(pk=pk).first()
