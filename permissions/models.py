from django.db import models


class Rotinas(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    descr = models.CharField(max_length=40)
    sit = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'rotinas'
