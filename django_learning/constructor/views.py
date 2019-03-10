from django.shortcuts import render
from .models import Ingredient
from .models import Group
from .forms import OrderForm


def constructor(request):
    # order_form = OrderForm()
    data = {
        "groups": Group.objects.all(),
        "ingredients": Ingredient.objects.all()
    }
    # return render(request, "index.html", {"order_form": order_form})
    return render(request, 'constructor/constructor.html', data)
