from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('reset/', views.reset_data, name='reset_data'),
]