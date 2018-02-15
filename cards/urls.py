from django.urls import path
from . import views

app_name='cards'
urlpatterns = [
    path('', views.SplashView.as_view(), name='splash'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.RegistrationView.as_view(), name='register'),
    path('thankyou', views.RegistrationLandingView.as_view(), name='landing'),
    path('checklogin', views.logged_in, name='checklogin')
]