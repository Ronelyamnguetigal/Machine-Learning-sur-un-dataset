from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'age', 'Tension', 'predictions')
admin.site.register(Data, DataAdmin)
