from django.contrib import admin

from .models import Question, Post, Board


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Post)

admin.site.register(Board)
