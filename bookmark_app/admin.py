from django.contrib import admin
from .models import Customer, BookMark

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  list_diplay = "__all__"
  list_filter = ['name']

class BookMarkAdmin(admin.ModelAdmin):
  list_display = ['title', 'source_name',]
  list_filter = ['date_added']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(BookMark, BookMarkAdmin)