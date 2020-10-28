from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

from queries.models import Query

class Question(models.Model):
    """
    Represents a question or inquiry that a person may ask.

    Questions may be answered by data or relate to other questions.
    """
    title = models.CharField(max_length=255, help_text="The question in short form.")
    description = models.TextField(help_text="Give a bit more detail about the question.", null=True, blank=True)
    keywords = TaggableManager()
    queries = models.ManyToManyField(Query)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})