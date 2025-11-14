from django.db import models

# Create your models here.

class Car(models.Model):
    """Model representing a car in the dealership."""
    
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('certified', 'Certified Pre-Owned'),
    ]
    
    make = models.CharField(max_length=100, help_text="Car manufacturer (e.g., Toyota, Ford)")
    model = models.CharField(max_length=100, help_text="Car model name")
    year = models.IntegerField(help_text="Manufacturing year")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used')
    color = models.CharField(max_length=50, blank=True)
    mileage = models.IntegerField(help_text="Mileage in miles", null=True, blank=True)
    description = models.TextField(blank=True)
    vin = models.CharField(max_length=17, unique=True, help_text="Vehicle Identification Number")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

