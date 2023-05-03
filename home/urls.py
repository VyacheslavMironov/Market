from django.urls import path
from .views import login, registration

urlpatterns = [
    path('login', login, name="urlLogin"),
    path('registration', registration, name="urlRegistration"),
]