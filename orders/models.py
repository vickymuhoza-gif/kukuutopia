from django.db import models

# Create your models here.
class Order(models.Model):
  ORDER_TYPE = (
    ('normal','Normal'),
    ('bulk','Bulk'),
  )

  STATUS=(
    ('pending','Pending'),
    ('confirmed','Confirmed'),
    ('completed','Completed'),
    ('cancelled','Cancelled'),
  )

  user = models.ForeignKey(
    'accounts.User',
    on_delete=models.CASCADE
  )
  location = models.ForeignKey(
    'accounts.Location',
    on_delete=models.SET_NULL,
    null=True
  )
  order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
  total_amount = models.DecimalField(max_digits=12, decimal_places=2)
  payment_status = models.CharField(max_length=20)
  order_status = models.CharField(max_length=20, choices=STATUS)
  delivery_distance = models.DecimalField(max_digits=6, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
  order = models.ForeignKey(
    Order,
    on_delete=models.CASCADE,
    related_name='items'
  )  
  product = models.ForeignKey(
    'products.Product',
    on_delete=models.CASCADE
  )
  quantity = models.PositiveIntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

class BulkOrder(models.Model):
  order = models.OneToOneField(
    Order,
    on_delete=models.CASCADE,
    related_name='bulk_details'
  )
  event_date = models.DateField()
  special_instructions = models.TextField(blank=True)
  advance_payment_required = models.BooleanField(default=False)

class Booking(models.Model):
  STATUS = (
    ('active','Active'),
    ('expired','Expired'),
    ('confirmed','Confirmed')
  )

  user = models.ForeignKey(
    'accounts.User',
    on_delete=models.CASCADE
  )

  product = models.ForeignKey(
    'products.Product',
    on_delete=models.CASCADE
  )

  quantity = models.PositiveIntegerField()
  reserved_until = models.DateTimeField()
  status = models.CharField(max_length=20, choices=STATUS)