# payments/urls.py

from django.urls import path
from .views import payment_view, success_view 

urlpatterns = [
    path('pay/', payment_view, name='payment'),
    path('success/', success_view, name='success'),
]


