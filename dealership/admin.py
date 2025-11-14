from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Admin interface for Car model."""
    list_display = ('make', 'model', 'year', 'price', 'condition', 'is_available', 'created_at')
    list_filter = ('condition', 'is_available', 'make', 'year')
    search_fields = ('make', 'model', 'vin', 'description')
    list_editable = ('is_available',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('make', 'model', 'year', 'vin')
        }),
        ('Details', {
            'fields': ('condition', 'color', 'mileage', 'description')
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'is_available')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

