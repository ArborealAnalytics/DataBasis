from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    model = Question