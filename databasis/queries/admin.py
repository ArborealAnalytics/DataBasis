from django.contrib import admin

from .models import Query


@admin.register(Query)
class QueryModelAdmin(admin.ModelAdmin):
    model = Query
    fields = ("title", "description", "sql")
