"""Admin configuration for company_profile app."""

from django.contrib import admin
from apps.company_profile.models import (
    Profile,
    Skill,
    SocialLink,
    Experience,
    Project,
    ProjectImage,
    ProjectTag,
    ContactMessage,
    StoredFile,
)


@admin.register(StoredFile)
class StoredFileAdmin(admin.ModelAdmin):
    list_display = ["name", "content_type", "size", "created_at"]
    search_fields = ["name", "content_type"]
    readonly_fields = ["name", "content_type", "size", "created_at", "updated_at"]



class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ["name", "level", "category", "icon", "order"]


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ["platform", "url", "icon_class", "order", "is_visible"]


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ["image", "caption", "order"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "tagline", "email", "is_active", "updated_at"]
    list_filter = ["is_active"]
    inlines = [SkillInline, SocialLinkInline]
    fieldsets = [
        ("Informasi Dasar", {"fields": ["full_name", "tagline", "bio", "bio_detail", "photo", "is_active"]}),
        ("Kontak", {"fields": ["email", "phone", "location"]}),
        ("Dokumen", {"fields": ["resume_file"]}),
    ]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["title", "organization", "type", "start_date", "end_date", "is_current"]
    list_filter = ["type", "is_current"]
    search_fields = ["title", "organization"]
    ordering = ["-start_date"]


@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "color"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "client", "status", "year", "is_featured", "is_visible", "order"]
    list_filter = ["status", "is_featured", "is_visible", "tags"]
    search_fields = ["title", "client", "short_description"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags"]
    inlines = [ProjectImageInline]
    fieldsets = [
        ("Info Proyek", {"fields": ["profile", "title", "slug", "client", "short_description", "description"]}),
        ("Visual", {"fields": ["cover_image", "tags"]}),
        ("Detail", {"fields": ["role", "status", "year", "url"]}),
        ("Tampilan", {"fields": ["is_featured", "is_visible", "order"]}),
    ]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "subject", "message"]
    readonly_fields = ["name", "email", "subject", "message", "ip_address", "created_at"]
    ordering = ["-created_at"]
