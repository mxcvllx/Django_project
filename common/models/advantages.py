from django.db import models


class Advantages(models.Model):
    title = models.CharField(max_length=400)

