from django.urls import path
from .views import platform, games, cart

urlpatterns = [
    path('', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]