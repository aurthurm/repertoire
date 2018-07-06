from django.db import models

class Order(models.Model):
    order_by = models.ForeignKey('auth.User', on_delete = models.PROTECT)
    ordering_dept = models.ForeignKey('laboratory.Department', related_name = 'order_from', on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order_state = models.BooleanField(default=False)
    order_number = models.CharField(max_length = 25, default = '',  unique = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='prdcts', on_delete = models.PROTECT)
    product =  models.ForeignKey('products.Product', related_name='order_prdcts', on_delete = models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
