from django.contrib import admin
from .models import *
# Register your models here.
#
class RecordAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone_number','city','state']

admin.site.register(Record,RecordAdmin)
