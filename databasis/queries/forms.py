from django import forms

from django_ace import AceWidget

from .models import Query


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = "__all__"
        labels = {
            "sql": "SQL",
        }
        widgets = {
            "sql": AceWidget(
                mode="sql",
                theme="twilight",
                width="100%",
                showinvisibles=True,
                toolbar=False,
            ),
        }