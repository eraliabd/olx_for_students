from django.urls import path
from .views import SignUpView, house, courtyard, apartment, contract, nocontract, travel, trip, library, food

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('house/', house, name='house'),
    path('house/courtyard/', courtyard, name='courtyard'),
    path('house/apartment/', apartment, name='apartment'),
    path('house/contract/', contract, name='contract'),
    path('house/nocontract/', nocontract, name='nocontract'),
    path('travel/', travel, name='travel'),
    path('travel/trip/', trip, name='trip'),
    path('travel/library/', library, name='library'),
    path('travel/food/', food, name='food'),
]
