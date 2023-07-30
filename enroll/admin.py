from django.contrib import admin
from enroll.models import studentdb
# Register your models here.

@admin.register(studentdb)
class studentdbAdmin(admin.ModelAdmin):
    list_display=['name','email','password']
