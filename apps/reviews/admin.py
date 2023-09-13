from django.contrib import admin
from apps.reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'grade', 'user', 'created_at', 'moderation')
    list_filter = ('hotel', 'grade', 'moderation')