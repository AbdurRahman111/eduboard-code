from django.contrib import admin
from .models import FormData

# Register your models here.

# admin.site.register(FormData)


@admin.register(FormData)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Question', 'Clue', 'Solution',
                    'Answer', 'CorrectAnswer','ImageData')
