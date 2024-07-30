from django.contrib import admin
from .models import DependencyData, DependencyDataArticle

@admin.register(DependencyData)
class DependencyDataAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'dep_svg_path')
    search_fields = ('sentence',)

@admin.register(DependencyDataArticle)
class DependencyDataArticleAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'dep_svg_path')
    search_fields = ('sentence',)
