from django.db import models

class GroceryList(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
