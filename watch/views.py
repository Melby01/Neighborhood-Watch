from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, ProfileForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
     form = RegistrationForm(request.POST)
     if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      messages.success(request,f'Account for {username} created,you can now login')
      login(request, user)
      return redirect('index.html')
    else:
      form = RegistrationForm()
    return render(request,'registration/register.html',{"form":form})
  
def profile(request):
    return render(request, 'profile.html')
  
def edit_profile(request):
    user = User.objects.get()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form =  ()
        
    return render(request, 'new_profile.html', {'form': form})

