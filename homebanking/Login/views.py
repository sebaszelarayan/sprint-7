from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.views.generic  import TemplateView
# Create your views here.
def Register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password= user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request,'register.html',data)
    
class LoginView(View):
    def get(self,request):
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})

    def post(self,request):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
        return render(request,'login.html',{'form':form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

class HomeView(TemplateView):
    template_name='home.html'