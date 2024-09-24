from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):
    class CategoryChoices(models.TextChoices):
        FOOD = 'FOOD', 'Ovqat'
        UNIVERSITY = 'UNIVERSITY', 'Universitet'
        PUBLICTRANSPORT = 'PUBLICTRANSPORT', 'Jamoat transporti'
        INTERNET = 'INTERNET', 'Internet'
        CLOTHING = 'CLOTHING', 'Kiyim'
        OTHER = 'OTHER', 'Boshqalar'


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=50, choices=CategoryChoices.choices, 
                                default=CategoryChoices.OTHER)
    description = models.TextField()
    date = models.DateField()
    
    
    class Meta:
        verbose_name = 'Xarajat'
        verbose_name_plural = 'Xarajatlar'
        
        
    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
    