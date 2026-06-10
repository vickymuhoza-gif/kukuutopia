from django.db import models

# Create your models here.
class Delivery(models.Model):
  order = models.OneToOneField(
    'orders.Order',
    on_delete=models.CASCADE
  )
  delivery_fee = models.DecimalField(max_digits=10,decimal_places=2)
  status = models.CharField(max_length=20)
  delivered_at = models.DateTimeField(null=True,blank=True)