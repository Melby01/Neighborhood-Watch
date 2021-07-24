from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
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
