from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views import generic
from .forms import RegistrationForm, LoginForm
from .models import WatermarkUser
from django.http import HttpResponseRedirect, HttpResponse

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

class RegistrationView(FormView):
    template_name = "cards/register.html"
    form_class = RegistrationForm
    success_url = "/thankyou"

    def form_valid(self, form):
        print("Valid form!")
        print(form.cleaned_data)
        data = form.cleaned_data
        # user = WatermarkUser(email=data['email'], username=data['username'], password=data['password1'])
        user = WatermarkUser.objects.create_user(email=data['email'],username=data['username'],password=data['password1'])
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
        return super().form_valid(form)

def logged_in(request):
    if request.user.is_authenticated:
        return HttpResponse("You're logged in")
    else:
        return HttpResponse("You're not logged in")
