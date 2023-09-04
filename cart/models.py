from django.db import models
from home.models import product, ProductVariant

# Create your models here.


class cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True, null=True)
    dateAdded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class cartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def subTotal(self):
        return self.variant.price * self.quantity

    def __str__(self):
        return str(self.cart.cart_id)


class customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class order(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    shipping = models.CharField(max_length=255)
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class orderItem(models.Model):
    order = models.ForeignKey(order,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='variant')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.item.name)

    def subTotal(self):
        return self.variant.price * self.quantity
