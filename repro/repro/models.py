from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField
from django.utils import timezone
from psycopg2 import _range as psycopg2_range

class TestModel(models.Model):
    range = DateTimeRangeField()


def test_range():
    d = timezone.now()
    t = TestModel(range=psycopg2_range.DateTimeTZRange(d, d))
    assert t.range.isempty is False
    assert t.range != psycopg2_range.DateTimeTZRange(empty=True)

    t.save()
    t.refresh_from_db()

    assert t.range.isempty is True
    assert t.range == psycopg2_range.DateTimeTZRange(empty=True)

    t.delete()

# test_range()