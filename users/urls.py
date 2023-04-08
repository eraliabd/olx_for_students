from django.urls import path
from .views import SignUpView, house, courtyard, apartment, contract, nocontract

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('house/', house, name='house'),
    path('house/courtyard/', courtyard, name='courtyard'),
    path('house/apartment/', apartment, name='apartment'),
    path('house/contract/', contract, name='contract'),
    path('house/nocontract/', nocontract, name='nocontract'),
]
