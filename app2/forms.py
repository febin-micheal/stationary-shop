from django.forms import ModelForm
from .models import *

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'store']