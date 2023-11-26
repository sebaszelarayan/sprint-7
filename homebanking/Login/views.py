from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout
from django.views import View
from django.views.generic  import TemplateView ,CreateView
from django.urls import reverse_lazy
# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"
    
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