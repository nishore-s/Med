from django.shortcuts import render,redirect, get_list_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Medicine

from .forms import MedicineForm
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"account craeated successfully.")
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,"signup.html",{form:form})    

        

             
  
  
    

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request,form.get_user )
            messages.success(request, "logged in successfully.")
            
            return redirect('medicine_list')

        else:
         messages.error(request,"Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def add_medicine(request):
    user_meds = Medicine.objects.filter(user=request.user)
    if user_meds.count() >= 5:
        messages.error(request, "You can only add up to 5 medicines.")
        return redirect('medicine_list')

    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            med = form.save(commit=False)
            med.user = request.user
            
            med.save()
            messages.success(request,"Medicine added successfully")
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})
@login_required
def medicine_list(request):
    query = request.GET.get('q')
    meds = Medicine.objects.filter(user=request.user)
    if query:
        meds = meds.filter(Q(name__icontains=query))

    paginator = Paginator(meds, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'medicine_list.html', {'page_obj': page_obj})
@login_required
def edit_medicine(request, pk):
    med = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == "POST":
        form = MedicineForm(request.POST, instance=Medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=med)
    return render(request, '/edit_medicine.html', {'form': form})
@login_required
def delete_medicine(request, pk):
    med = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == "POST":
        Medicine.delete()
        return redirect('medicine_list')
    return render(request, '/delete_medicine.html', {'med': med})







# Create your views here.
