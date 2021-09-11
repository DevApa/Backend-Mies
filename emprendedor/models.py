from django.db import models
from entrepreneur.CHICES import TypeIdentify


class Entrepreneur(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_emprendedor')
    code = models.CharField(max_length=45, blank=True, null=True, unique=True, db_column='codigo_mies')
    identify = models.CharField(max_length=45, blank=True, null=True, unique=True, db_column='identificacion')
    type_identify = models.CharField(max_length=45, choices=TypeIdentify, blank=True, null=True, db_column='tipo_identificacion')
    phone = models.CharField(max_length=45, blank=True, null=True, db_column='telefono')
    barrio = models.CharField(max_length=45, blank=True, null=True, db_column='barrio')
    sector = models.CharField(max_length=45, blank=True, null=True, db_column='sector')
    address = models.CharField(max_length=45, blank=True, null=True, db_column='domicilio')
    user = models.ForeignKey('entrepreneur.Usuario', db_column='id_usuario', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, blank=True, null=True, db_column='status')

    def __str__(self):
        return self.identify

    class Meta:
        db_table = 'tbl_emprendedor'
