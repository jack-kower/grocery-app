from django.shortcuts import render
from django.views import View


def index(request):
    name = 'Jack'
    return render(request, "index.html", {"name": name})

def grocery_list(request):
    return render(request, "grocery-list.html")
