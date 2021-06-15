from django.db import models

# Create your models here.


class Aliquotas(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    instit = models.PositiveIntegerField()
    descr = models.CharField(max_length=6)
    bematech = models.CharField(max_length=2)
    valor = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aliquotas'
        unique_together = (('instit', 'descr'),)
