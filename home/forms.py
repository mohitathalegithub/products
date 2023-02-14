from django import forms
from models import product

class product(forms.modelform):
    class Meta:
        model=product
        fields=['name','discription','price']
        