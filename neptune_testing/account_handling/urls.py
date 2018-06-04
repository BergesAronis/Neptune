from django.urls import path

from . import views
app_name = 'account_handling'
urlpatterns = [
    path('registration', views.account_registration, name='registration'),
    path('login', views.account_login, name='login'),
]
