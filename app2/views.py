from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home.html')

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
    template_name = 'store.html'
    model = Store
    success_url = 'store_list'
    fields = ['id', 'name']
    template_edit = 'store_update.html'

class ItemView(ModelView):
    form_class = ItemForm
    template_name = 'item.html'
    model = Item
    success_url = 'item_list'
    fields = ['id', 'name', 'store__name']
    template_edit = 'item_update.html'
