from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def store(request, pk = None):

    if request.method == 'GET':
        if pk != None:
            store = Store.objects.get(id = pk)
            store.delete()

        form = StoreForm
        store_list = list(Store.objects.all().values())
        page = {
            'form': form,
            'store_list': store_list
        }

        return render(request, 'app2/store.html', page)

    elif request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            Store.objects.create(**form.cleaned_data)
        
        return redirect('store')

def item(request, pk = None):

    if request.method == 'GET':
        if pk != None:
            item = Item.objects.get(id = pk)
            item.delete()

        form = ItemForm
        item_list = list(Item.objects.all().values())
        item_store = list(Item.objects.all().values("store__name"))
        page = {
            'form': form,
            'item_list': item_list
        }

        return render(request, 'app2/item.html', page)

    elif request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item.objects.create(**form.cleaned_data)
        
        return redirect('item')
