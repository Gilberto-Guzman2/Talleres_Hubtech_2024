from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'content']

admin.site.register(Review, ReviewAdmin)