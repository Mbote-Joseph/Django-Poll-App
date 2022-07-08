from calendar import c
from datetime import datetime, timezone
from django.contrib import admin
from . import models

# Register your models here.
class Question(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

   

class Choice(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')
    search_fields = ['choice_text']

   

admin.site.register(models.Question)
admin.site.register(models.Choice)