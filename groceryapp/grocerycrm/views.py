from django.shortcuts import render
from django.views import View
from .models import GroceryList
from django.contrib import messages
from django.db.models import Count, Avg

def index(request):
    name = 'Jack'
    return render(request, "index.html", {"name": name})

def add_grocery(request):
    is_submitted = False
    new_item = ""
    if request.method == "POST":
        item_name = request.POST["item-name"]
        price = request.POST["item-price"]
        quantity = request.POST["quantity"]

        new_item = GroceryList(item_name=item_name, item_price=price, 
                               quantity=quantity)
        new_item.save()
        is_submitted=True
    if is_submitted==True:
        messages.success(request, "Submitted Successfully!")

    return render(request, "add-grocery.html", {"new_item": new_item})

def grocery_list(request):
    list = GroceryList.objects.all()
    counter = list.count()

    price = GroceryList.objects.all()


    return render(request, "grocery-list.html", {"list": list, 
                                                 "counter": counter, 
                                                 "price": price,
                                                 })
