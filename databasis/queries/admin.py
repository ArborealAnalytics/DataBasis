from django import forms
from django.contrib import admin

from django_ace import AceWidget

from .models import Query


class QueryModelAdminForm(forms.ModelForm):
    class Meta:
        model = Query
        widgets = {"sql": AceWidget(mode="sql", toolbar=False)}
        fields = "__all__"


@admin.register(Query)
class QueryModelAdmin(admin.ModelAdmin):
    form = QueryModelAdminForm