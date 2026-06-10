from django.db import models
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.utils import timezone

# Create your models here.

class Location(models.Model):
  city = models.CharField(max_length=100)
  district = models.CharField(max_length=100)
  address = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.city},{self.district}"
  
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('farmer', 'Farmer'),
        ('vendor', 'Vendor'),
    ]
    
    location = models.ForeignKey(
        'Location', 
        on_delete=models.SET_NULL, 
        null=True, 
        db_column='location_id',
        related_name='users'
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)  # Changed to 20 for international numbers
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.full_name
  
class Contact(models.Model):
  CONTACT_TYPE = (
    ('phone','Phone'),
    ('whatsapp','WhatsApp'),
    ('email','Email'),
  )

  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='contacts')
  type = models.CharField(max_length=20, choices=CONTACT_TYPE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return f"Contact from {self.user.full_name} ({self.type})"


class Notification(models.Model):
  NOTIFICATION_TYPE_CHOICES = [
    ('order', 'Order'),
    ('account', 'Account'),
    ('delivery', 'Delivery'),
    ('promotion', 'Promotion'),
    ('other', 'Other'),
  ]

  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='notifications'
  )
  title = models.CharField(max_length=255)
  message = models.TextField()
  notification_type = models.CharField(
    max_length=50,
    choices=NOTIFICATION_TYPE_CHOICES,
    default='other'
  )
  is_read = models.BooleanField(default=False)
  metadata = models.JSONField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Notification for {self.user.full_name}: {self.title}"
