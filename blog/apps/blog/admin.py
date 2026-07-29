"""Admin configuration for blog app."""

from django.contrib import admin
from apps.blog.models import Post, Category, Tag, ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "email", "subject", "message"]
    readonly_fields = ["created_at", "ip_address"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "color", "order"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status", "published_at", "created_at"]
    list_filter = ["status", "category", "tags"]
    search_fields = ["title", "excerpt", "body"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "published_at"
    ordering = ["-created_at"]
    fieldsets = [
        ("Konten", {"fields": ["title", "slug", "excerpt", "body"]}),
        ("Media", {"fields": ["cover_image"]}),
        ("Klasifikasi", {"fields": ["category", "tags"]}),
        ("Publikasi", {"fields": ["status", "published_at"]}),
        ("Metadata", {"fields": ["created_at", "updated_at"], "classes": ["collapse"]}),
    ]
