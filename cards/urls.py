from django.urls import path
from . import views

app_name='cards'
urlpatterns = [
    path('', views.SplashView.as_view(), name='splash'),
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.RegistrationView.as_view(), name='register'),
    path('thankyou', views.RegistrationLandingView.as_view(), name='landing'),
    path('checklogin', views.logged_in, name='checklogin'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('create_card', views.create_card, name='card-create'),
    path('delete_card', views.delete_card, name='card-delete'),
    path('card/<str:id>', views.CardDetailView.as_view(), name='card-detail'),
    path('wallet/<int:id>', views.WalletDetailView.as_view(),name='wallet-detail'),
    # path('wallets'),
]