from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth import authenticate, login
from .models import Category, InventoryItem
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import UserRegisterForm
from .forms import InventoryItemForm
# Create your views here
def Index(request):
    return render(request, 'inventory/index.html')

class Dashboard(LoginRequiredMixin,View):
    def get(self, request):
        items=InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        return render(request, 'inventory/dashboard.html', {'items':items})

class SignUpView(View):
    def get(self,request):
        form=UserRegisterForm()  
        return render(request,'inventory/signup.html',{'form':form})      


    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
        return render(request,'inventory/signup.html',{'form':form})
class AddItem(LoginRequiredMixin,CreateView):
    model=InventoryItem
    form_class=InventoryItemForm
    template_name='inventory/add_item.html'
    success_url='/dashboard/'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context  
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class EditItem(LoginRequiredMixin,UpdateView):
    model=InventoryItem
    form_class=InventoryItemForm
    template_name='inventory/add_item.html'
    success_url=reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin,View):
    model=InventoryItem
    template_name='inventory/delete_item.html'
    
    success_url=reverse_lazy('dashboard')
    context_object_name='item'