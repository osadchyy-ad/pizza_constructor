from django import forms


class OrderForm(forms.Form):
    total_price = forms.FloatField()
