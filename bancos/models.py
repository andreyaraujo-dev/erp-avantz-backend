from django.db import models

# Create your models here.


class Bancos(models.Model):
    id_bancos = models.IntegerField(primary_key=True)
    cod = models.PositiveIntegerField()
    banco = models.CharField(max_length=50)
    # Field name made lowercase.
    ispb = models.PositiveIntegerField(db_column='ISPB')
    compens = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bancos'
