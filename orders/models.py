from django.db import models
from users.models import CustomUser
from catalog.models import Product
from payment.models import PaymentTransaction


class Order(models.Model):
    status = (('Paid', 'Paid'),
                      ('Unpaid', 'Unpaid'),
                      ('Pending', 'Pending'))
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_transaction = models.ForeignKey(PaymentTransaction, on_delete=models.CASCADE)
    paid = models.CharField(choices=status, max_length=20)
    total_price = 1


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'




class OrderItem(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)



