from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Posts, UserProfile, Nachrichten

admin.site.register(Posts)
admin.site.register(UserProfile)
admin.site.register(Nachrichten)