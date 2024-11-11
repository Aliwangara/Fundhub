from django.contrib import admin
from investor_profile.models import *
# Register your models here.
admin.site.register(investor_profile)
admin.site.register(Conversation)
admin.site.register(Message)