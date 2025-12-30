from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # <--- Tambahan baru

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('IN', 'Pemasukan'),
        ('OUT', 'Pengeluaran'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    
    date = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"