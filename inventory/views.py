from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth import authenticate, login
from .models import InventoryItem

from .forms import UserRegisterForm
# Create your views here
def Index(request):
    return render(request, 'inventory/index.html')

class Dashboard(View):
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