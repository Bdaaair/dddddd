from django.db import models

class  Restaurants(models.Model):
    name = models.CharField(max_length=30),
    description = models.CharField(),
    opening_time = models.TimeField(),
    closing_time = models.TimeField(),
    created_at = models.DateTimeField()

