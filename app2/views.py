from re import template
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home(request):
    return render(request, 'app2/home.html')

def store(request, pk = None):
    if pk != None:
        store = Store.objects.get(id = pk)
        if request.POST.get('method') == 'delete':
            store.delete()

        elif request.POST.get('method') == 'edit':
            form = StoreForm(instance = store)

            return render(request, 'app2/store_update.html', {'form': form, 'store': store})  

        elif request.POST.get('method') == 'update':
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
        if request.POST.get('method') == 'delete':
            item.delete()

        elif request.POST.get('method') == 'edit':
            form = ItemForm(instance = item)

            return render(request, 'app2/item_update.html', {'form': form, 'item': item})  

        elif request.POST.get('method') == 'update':
            form = ItemForm(request.POST, instance = item)
            if form.is_valid():
                form.save()          

    else:  
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    form = ItemForm
    item_list = list(Item.objects.all().values('id', 'name', 'store__name'))

    page = {
        'form': form,
        'item_list': item_list,
    }

    return render(request, 'app2/item.html', page)

from django.views import View

class ModelView(View):
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        object_list = list(self.model.objects.all().values(*self.fields))
        page = {
            'form': form,
            'object_list': object_list
        }
        return render(request, self.template_name, page)

    def post(self, request, pk = None, *args, **kwargs):
        
        if pk == None:
            form = self.form_class(request.POST)
            if form.is_valid():
                self.model.objects.create(**form.cleaned_data)
        
        else:
            object = self.model.objects.get(id = pk)
            if request.POST.get('method') == 'delete':
                object.delete()

            elif request.POST.get('method') == 'edit':
                form = self.form_class(instance = object)

                return render(request, self.template_edit, {'form': form, 'object': object})  

            elif request.POST.get('method') == 'update':
                form = self.form_class(request.POST, instance = object)
                if form.is_valid():
                    form.save()          


        return redirect(self.success_url)
        

class StoreView(ModelView):
    form_class = StoreForm
    template_name = 'app2/store.html'
    model = Store
    success_url = 'store'
    fields = ['id', 'name']
    template_edit = 'app2/store_update.html'

class ItemView(ModelView):
    form_class = ItemForm
    template_name = 'app2/item.html'
    model = Item
    success_url = 'item'
    fields = ['id', 'name', 'store__name']
    template_edit = 'app2/item_update.html'
