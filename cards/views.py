from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views import generic
from .forms import RegistrationForm, LoginForm
from .models import WatermarkUser, UserCard, Wallet
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from time import time

import json

class SplashView(TemplateView):
    template_name = "cards/splash.html"

class RegistrationLandingView(TemplateView):
    template_name = "cards/landing.html"

class RegisterView(TemplateView):
    template_name = "cards/register.html"

class WalletView(generic.ListView):
    template_name = "cards/wallet.html"

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponseRedirect('/')
#     else:
#         form = UserCreationForm()

#     return render(request, 'cards/register.html', {'form' : form})

class ProfileView(generic.TemplateView):
    template_name = "cards/profile.html"

    def get_cards(self):
        user = WatermarkUser.objects.get(username = self.request.user)
        return user.usercard_set.all()

    def default_card(self):
        user = WatermarkUser.objects.get(username=self.request.user)
        return user.profile.default_card.id


def get_cards(request):
    if request.user:
        user = WatermarkUser.objects.get(username=request.user)


def create_card(request):
    if request.user:
        user = WatermarkUser.objects.get(username=request.user)
        print("Making a card for ", request.user)
        card = UserCard.objects.create(owner=user)
        if (user.profile.default_card is None):
            user.profile.default_card = card
            user.profile.save()
        data = json.loads(request.body)
        print(data['name'])

    return JsonResponse({'success': True})

def delete_card(request):
    if request.user:
        data = json.loads(request.body)
        user = WatermarkUser.objects.get(username=request.user)
        card = UserCard.objects.get(id=data['id'])
        card.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

class RegistrationView(FormView):
    template_name = "cards/register.html"
    form_class = RegistrationForm
    success_url = "/thankyou"

    def form_valid(self, form):
        print("Valid form!")
        data = form.cleaned_data
        user = WatermarkUser.objects.create_user(email=data['email'],username=data['username'],password=data['password1'])
        user.profile.first_name = data['first_name']
        user.profile.last_name = data['last_name']
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("NOT VALID")
        print(form.cleaned_data)
        return super().form_invalid(form)

class LoginView(FormView):
    template_name = "cards/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        print("Login submitted")
        print(form.cleaned_data)
        data = form.cleaned_data
        user = authenticate(self.request, username=data['username'], password=data['password'])
        if user is not None:
            login(self.request, user)
            print('Login successful')
        else:
            print('Login unsuccessful')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("failed")
        print(form.cleaned_data)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['time'] = time()
        return context

def logged_in(request):
    if request.user.is_authenticated:
        return HttpResponse("You're logged in as {}".format(request.user.username))
    else:
        return HttpResponse("You're not logged in")
