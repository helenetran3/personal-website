from django.contrib import admin

from .models import Project, Teammate, ProgrammingLanguage

class TeammateInline(admin.TabularInline):
    model = Teammate

class LanguageInline(admin.TabularInline):
    model = ProgrammingLanguage

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_name', 'description', 'website_link']}), # 'languages',
        ('Date information', {'fields': ['date_start', 'date_end', 'duration']}),
        ('Location', {'fields': ['location_city', 'location_country']})
    ]
    inlines = [TeammateInline]#, LanguageInline]
    search_fields = ['project_name']

admin.site.register(Project, ProjectAdmin)
