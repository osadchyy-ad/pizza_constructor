from django.contrib import admin
from .models import Ingredient
from .models import Group

admin.site.register(Ingredient)
admin.site.register(Group)
# Register your models here.
