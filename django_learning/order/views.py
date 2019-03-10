from django.shortcuts import render
from django.http import HttpResponse
from constructor.models import Ingredient


def order(request):
    if request.method == "POST":
        ings = Ingredient.objects.all()
        orderlist = dict(request.POST.lists())
        total = 0
        for ing in ings:
            total += int(orderlist[str(ing.id)][0]) * ing.price

        data = {
            'total': total
        }
        return render(request, 'order/order.html', data)
    elif request.method == 'GET':
        return HttpResponse('<h1>No order</h1>')

# request.content_params
# Create your views here.
