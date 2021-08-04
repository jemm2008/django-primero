from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs/")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de TODOS los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo FORMULARIO para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, numero):
    return HttpResponse("Placeholder para mostrar el blog  " + str(numero))

def edit(request, numero):
    return HttpResponse("Placeholder para EDITAR el Blog  " + str(numero))

def destroy(request, numero):
    return redirect("/blogs/")

def json(request):
    AxieInfinity = {
        "Nombre": "Blog AXS",
        "Coin": 'AXS',
        "Listed in": ["Binance", "Uniswap", "Coinmarketcap", "Coingeko"],
        "Hight Value in 2.021 in USD": 53.28,
    }
    return JsonResponse(AxieInfinity)
