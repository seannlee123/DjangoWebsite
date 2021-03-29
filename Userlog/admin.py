
from django.contrib import admin

# Register your models here.

#Register model to admin site
from .models import  UserTopic, Entry,Tag
admin.site.register(UserTopic)
admin.site.register(Entry)
admin.site.register(Tag)

