from django.contrib import admin

# Register your models here.

#Register model to admin site
from Userlog.models import UserTopic
admin.site.register(UserTopic)