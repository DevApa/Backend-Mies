from django.db import models


class TypeActivityEconomic(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', unique=True)
    name = models.CharField(max_length=45, blank=True, null=True, db_column='nombre')
    description = models.CharField(max_length=45, blank=True, null=True, db_column='descripcion')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_tipo_actividad_economica'
