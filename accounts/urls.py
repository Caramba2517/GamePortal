from django.urls import path, include
from .views import profile

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', profile, name='profile'),
]