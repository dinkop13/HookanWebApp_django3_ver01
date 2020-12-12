from django.contrib import admin

# Register your models here.
from .models import Items, Shops, Storage

admin.site.register(Items)
admin.site.register(Shops)
admin.site.register(Storage)
