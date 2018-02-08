from django.urls import path
from . import views

app_name='cards'
urlpatterns = [
    path('', views.SplashView.as_view(), name='splash'),
    path('/login', name='login')
]