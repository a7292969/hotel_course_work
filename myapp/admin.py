from django.contrib import admin

from .models import Comment, Room

admin.site.register(Room)
admin.site.register(Comment)