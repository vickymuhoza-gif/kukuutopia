from django.db import models

# Create your models here.
class Product(models.Model):
  category = models.ForeignKey(
    'categories.Category',
    on_delete=models.CASCADE,
    related_name='products'
  )
  name = models.CharField(max_length=200)
  description = models.TextField()
  unit = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products/', null=True, blank=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.name
  
class Inventory(models.Model):
  product =  models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='inventory'
  )
  managed_by = models.ForeignKey(
    'accounts.User',
    on_delete=models.SET_NULL,
    null= True
  )
  quantity_available = models.PositiveIntegerField()
  cost_price = models.DecimalField(max_digits=10, decimal_places=2)
  expiry_date = models.DateField(null=True, blank = True)
  added_at = models.DateTimeField(auto_now_add=True)