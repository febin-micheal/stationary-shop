from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def store(request, pk = None):
    if pk != None:
        store = Store.objects.get(id = pk)
        if request.POST.get('delete') == 'delete':
            store.delete()

        elif request.POST.get('edit') == 'edit':
            form = StoreForm(instance = store)

            return render(request, 'app2/store_update.html', {'form': form, 'store': store})  

        elif request.POST.get('update') == 'update':
            form = StoreForm(request.POST, instance = store)
            if form.is_valid():
                form.save()          

    else:  
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()

    form = StoreForm
    store_list = list(Store.objects.all().values())
    page = {
        'form': form,
        'store_list': store_list
    }

    return render(request, 'app2/store.html', page)

def item(request, pk = None):
    if pk != None:
        item = Item.objects.get(id = pk)
        if request.POST.get('delete') == 'delete':
            item.delete()

        elif request.POST.get('edit') == 'edit':
            form = ItemForm(instance = item)

            return render(request, 'app2/item_update.html', {'form': form, 'item': item})  

        elif request.POST.get('update') == 'update':
            form = ItemForm(request.POST, instance = item)
            if form.is_valid():
                form.save()          

    else:  
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    form = ItemForm
    item_list = list(Item.objects.all().values())
    store_list = list(Store.objects.all().values())
    for item in item_list:
        for store in store_list:
            if item['store_id'] == store['id']:
                item['store__name'] = store['name']
    page = {
        'form': form,
        'item_list': item_list,
    }

    return render(request, 'app2/item.html', page)
