from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

class TestModel(models.Model):
    range = DateTimeRangeField()
