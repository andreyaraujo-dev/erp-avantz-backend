from django.db import models


class Rotinas(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='Id', primary_key=True)
    descr = models.CharField(max_length=40)
    sit = models.PositiveIntegerField()
    ordem = models.IntegerField()
    posicao_rotina = models.IntegerField()
    modulo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rotinas'
        ordering = ['ordem']

    def __str__(self):
        return self.descr
