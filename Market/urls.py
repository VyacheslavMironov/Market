
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('shop/', include("shop.urls")),
    path('basket/', include("basket.urls"))
]
