from django.urls import path

from . import views
app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('to_do_list', views.to_do_list, name='to_do_list'),
]
