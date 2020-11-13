from django.db import models

from simple_history.models import HistoricalRecords


class Query(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sql = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Queries"
