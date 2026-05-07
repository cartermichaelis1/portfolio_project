from django.contrib import admin
from .models import Project, Skill, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'summary', 'tools_used')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'slug', 'category', 'is_featured')}),
        ('Content', {'fields': ('summary', 'business_problem', 'tools_used', 'key_features', 'role_contribution', 'biggest_challenge', 'lessons_learned')}),
        ('Images', {'fields': ('image', 'image_two')}),
        ('Links', {'fields': ('github_link', 'demo_link')}),
        ('Metadata', {'fields': ('created_at',)}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')
