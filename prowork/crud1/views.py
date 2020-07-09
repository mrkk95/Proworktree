from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from crud1.models import dashboard
from django.contrib import messages
from datetime import datetime

# Create your views here.

def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    if(request.method == "POST"):
        acc_name=request.POST.get('acc_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')  
        form1=dashboard(acc_name=acc_name,email=email,phone=phone,desc=desc,date= datetime.today())
        form1.save()
        messages.success(request, 'Details has been sent to the owner of this site!')
    return render(request, 'dashboard.html')

def registerView(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})