from django.db import models


class Difficulty(models.Model):
    level = models.IntegerField(unique=True, null=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description