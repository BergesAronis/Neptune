from django.urls import path

from . import views
app_name = 'account_handling'
urlpatterns = [
    path('registration', views.account_registration, name='registration'),
    path('client_registration', views.client_registration, name='client_registration'),
    path('staff_registration', views.staff_registration, name='staff_registration'),
    path('agent_registration', views.agent_registration, name='agent_registration'),
    path('login', views.account_login, name='login'),
    path('logout', views.account_logout, name='logout'),
]
