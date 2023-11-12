from django.contrib import admin
from grocerycrm.models import GroceryList

class GroceryListAdmin(admin.ModelAdmin):
    list_display=["id","item_name","item_price", "quantity"]

admin.site.register(GroceryList, GroceryListAdmin)
