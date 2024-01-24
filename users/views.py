from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,UpdateUserForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.


def homepage_view(request):
    return render(request,'home.html')


def profile_view(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'users/profile.html',context=context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request,'users/editprofile.html',{'form':form})


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            form = login(request,user)
            return redirect('home')
    
    form = AuthenticationForm()

    return render(request,'registration/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')