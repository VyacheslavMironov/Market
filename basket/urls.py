from django.urls import path
from .views import index

urlpatterns = [
    path('basket', index, name="urlBasket"),    
]