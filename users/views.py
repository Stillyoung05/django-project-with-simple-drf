from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import SignUpForm,UpdateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def homepage_view(request):
    return render(request,'home.html')

@login_required
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

class CustomUserSignup(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            return redirect('login')
        
        context = {
            'form': form,
        }
        return render(request, 'registration/signup.html', context)


class CustomUserLogin(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    
            return redirect('home')
        
        
class CustomLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')