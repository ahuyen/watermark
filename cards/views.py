from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from .forms import UserCreationForm
from django.http import HttpResponseRedirect

class SplashView(TemplateView):
    template_name = "cards/splash.html"

class LoginView(TemplateView):
    template_name = "cards/login.html"

class RegisterView(TemplateView):
    template_name = "cards/register.html"

class WalletView(generic.ListView):
    template_name = "cards/wallet.html"

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'cards/register.html', {'form' : form})