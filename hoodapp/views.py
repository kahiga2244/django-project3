from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,UpdateUserForm,NeighbourHoodForm
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


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'prof_form': prof_form})

def create_hoodz(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('mahoodz')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhoodz.html', {'form': form})


def post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    post = Post.objects.filter(neighbourhood=hood)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.neighbourhood = hood
            form.user = request.user.profile
            form.save()
            return redirect('post', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'post': post,'form':form})

def business(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=mtaa)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.neighbourhood = hood
            form.user = request.user.profile
            form.save()
            return redirect('business', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'business': business,'form':form})


def search(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        search = Business.objects.filter(name__icontains=name).all()
        message = f'name'
        return render(request, 'search.html', {'search': search,'message': message  })
    else:
        message = "You haven't searched for any image category"
    return render(request, "search.html")

