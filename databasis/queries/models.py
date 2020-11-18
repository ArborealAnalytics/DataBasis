from django.db import models

from simple_history.models import HistoricalRecords
from taggit.managers import TaggableManager


class Query(models.Model):
    """
    Represents a database query. 
    
    The query may be related to a question, as a means of providing insight.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    sql = models.TextField()
    history = HistoricalRecords()
    keywords = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Queries"
