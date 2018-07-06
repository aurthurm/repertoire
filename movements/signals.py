from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from products.models import Product
from .models import Transaction, Adjustment


# method for updating
@receiver(pre_save, sender=Transaction, dispatch_uid="update_product_count")
def update_product(sender, instance, **kwargs):
    test_value = instance.product.remaining
    test_value -= instance.issued
    if test_value < 0:
    	raise ValidationError({'remaining':'Sorry you cant issue beyond what you have'})
    else:
        instance.product.remaining -= instance.issued
        instance.product.save()


# method for updating
@receiver(pre_save, sender=Adjustment, dispatch_uid="update_product_count")
def save_product(sender, instance, **kwargs):
    if instance.adjustment_type == 'TRANSFER IN':
        instance.product.remaining += instance.adjust
        instance.product.save()
    else:
        test_value = instance.product.remaining
        test_value -= instance.adjust
        if test_value < 0:
            raise ValidationError({'remaining':'Sorry you cant transact beyond what you have'})
        else:
            instance.product.remaining -= instance.adjust
            instance.product.save()
