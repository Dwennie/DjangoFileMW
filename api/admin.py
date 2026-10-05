from django.contrib import admin
from .models import Contact, PortfolioContact, Topic


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")


@admin.register(PortfolioContact)
class PortfolioContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "portfolio_url", "created_at")
    search_fields = ("name", "email", "subject", "portfolio_url")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "created_at")
    search_fields = ("name", "category", "description")
    list_filter = ("category",)
    ordering = ("id",)