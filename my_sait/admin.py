from django.contrib.auth.admin import UserAdmin

from .models import *
from django.contrib import admin

admin.site.register(UserProfile)

admin.site.register(TrpoPractices)
admin.site.register(TrpoLectures)
admin.site.register(PP0102Lectures)
admin.site.register(PP0102Practices)
admin.site.register(PP0201Lectures)
admin.site.register(PP0201Practices)
admin.site.register(Groups)
admin.site.register(Marks)
admin.site.register(Items)
