from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "reviewer",
        "rating",
    )
