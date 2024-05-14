from django.db import models
from customer.models import MenuItem

class Employee:
    """ Restaurant's end operation """

    def addfooditem(self, name, price, category):
        """ Insert a new food category """

        item = MenuItem(
            name=name,
            price=price,
            category = category
            )
        item.save()
        return item