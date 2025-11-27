from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "publish_date", "was_published_recently"]
    list_filter = ["publish_date"]
    fieldsets = [
        (None, {"fields": ['question_text']}),
        ("Date information", {"fields": ["publish_date"], "classes": ["collapse"]})
    ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

