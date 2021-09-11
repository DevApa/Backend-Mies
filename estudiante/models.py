from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_estudiante')
    name = models.CharField(max_length=45, blank=True, null=True, db_column='nombre')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_estudiante'
