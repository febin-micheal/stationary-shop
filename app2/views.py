from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home.html')

class ModelView(View):
    
    def __init__(self):
        self.page = {
            'form': self.form_class,
            'success_url': self.success_url,
            'button': 'Insert'
        }

    def get(self, request, *args, **kwargs):
        self.page['object_list'] = list(self.model.objects.all().values(*self.fields))

        return render(request, self.template_name, self.page)

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
                self.page['form'] = self.form_class(instance = object)
                self.page['button'] = 'Update'
                self.page['success_url'] = self.update_url
                self.page['id'] = object.id

            elif request.POST.get('method') == 'update':
                form = self.form_class(request.POST, instance = object)
                if form.is_valid():
                    form.save()          

        return self.get(request, *args, **kwargs)
        
class StoreView(ModelView):
    form_class = StoreForm
    template_name = 'store.html'
    model = Store
    fields = ['id', 'name']
    success_url = '/store/'
    update_url = '/store/update/'

class ItemView(ModelView):
    form_class = ItemForm
    template_name = 'item.html'
    model = Item
    fields = ['id', 'name', 'store__name']
    success_url = '/item/'
    update_url = '/item/update/'
