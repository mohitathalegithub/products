from django.db import models

# Create your models here.

class product(models.Model):
    productname=models.CharField(max_length=30)
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=6)

    def __str__(self):
        return self.productname + self.discription
    
