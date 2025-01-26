from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ShopOwnerSignUpForm

# Sign-Up View
def register(request):
    if request.method == 'POST':
        form = ShopOwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after signup
        else:
            print(form.errors)  # Debugging: Print form errors in terminal
    else:
        form = ShopOwnerSignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

    
# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Home View
def home(request):
    return render(request, 'accounts/home.html')
