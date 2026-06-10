from django.db import models

# Create your models here.
class Payment(models.Model):
  order = models.ForeignKey(
    'orders.Order',
    on_delete=models.CASCADE,
    related_name='payments'
  )

  method = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  transaction_reference = models.CharField(max_length=100)
  status = models.CharField(max_length=20)
  paid_at = models.DateTimeField(auto_now_add=True)