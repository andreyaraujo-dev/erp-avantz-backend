from django.db import models


class UsersGrp(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=15)
    instit = models.IntegerField()
    acess = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_grp'
        unique_together = (('instit', 'grupo'),)

    def __str__(self):
        return self.grupo
