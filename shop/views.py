from django.shortcuts import render
from .models import ShopModel

# Create your views here.
def index(request):
    return render(request, 'home.html', 
        {'lists': ShopModel.objects.all()})

def create(request):
    message = None
    if request.method == "POST":
        shop = ShopModel.objects.create(
            Title = request.POST["title"], 
            Description = request.POST["description"],
            Price = 123
        )
        
        if shop.save():
            message = "Данные успешно добавлены!"
        else:
            message = "Ошибка добавления данных"

    return render(request, 'admin/create.html', {"message": message})

def show(request):
    return render(request, 'admin/show.html')