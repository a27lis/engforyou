from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    
    fieldsets = (
        ('Resource', {
            'fields': ('title', 'link', 'description'),
            'classes': ('wide',)
        }),
        ('Styles', {
            'fields': (
                'learning_style_V',
                'learning_style_A',
                'learning_style_R',
                'learning_style_K'
            ),
            'classes': ('collapse',)
        }),
        ('Age Group', {
            'fields': (
                'age_group_kid',
                'age_group_young',
                'age_group_student',
                'age_group_adult',
                'age_group_mature'
            ),
            'classes': ('collapse',)
        })
    )

    list_display = [
        'title',
        'link',
        'description',
        'learning_style_V',
        'learning_style_A',
        'learning_style_R',
        'learning_style_K',
        'age_group_kid',
        'age_group_young',
        'age_group_student',
        'age_group_adult',
        'age_group_mature'
    ]
    
    # Поиск будет производиться по этим полям
    search_fields = ['title', 'description']
    
    
   