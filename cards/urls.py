from django.urls import path
from . import views

app_name='cards'
urlpatterns = [
    path('', views.SplashView.as_view(), name='splash'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.register, name='register')
]