from django.contrib import admin
from grocery.models import *

# Register your models here.
admin.site.register(List)
admin.site.register(Item)
admin.site.register(List_Item)