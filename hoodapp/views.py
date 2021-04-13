from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Create your views here.
@login_required(login_url='login')
def index(request):
     return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']

            send_welcome_email(username=username,email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form}) 


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')
