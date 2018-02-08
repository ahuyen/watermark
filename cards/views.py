from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic

class SplashView(TemplateView):
    template_name = "cards/splash.html"

class LoginView(TemplateView):
    template_name = "cards/login.html"

class WalletView(generic.ListView):
    template_name = "cards/wallet.html"