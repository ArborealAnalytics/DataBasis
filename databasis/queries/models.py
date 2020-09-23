from django.db import models


class Query(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sql = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Queries"
