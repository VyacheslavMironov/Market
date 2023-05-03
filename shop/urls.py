from django.urls import path
from .views import index, create, show

urlpatterns = [
    path('', index, name="urlHome"),
    path('admin/create/', create, name="urlCreate"),
    path('admin/show/', show, name="urlShow"),
]