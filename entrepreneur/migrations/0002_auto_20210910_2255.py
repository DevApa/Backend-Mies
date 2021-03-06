# Generated by Django 3.2.4 on 2021-09-11 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprendedor', '0002_entrepreneur_user'),
        ('entrepreneur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bond',
            name='entrepreneurship',
        ),
        migrations.AddField(
            model_name='bond',
            name='entrepreneur',
            field=models.ForeignKey(db_column='id_emprendedor', default=1, on_delete=django.db.models.deletion.CASCADE, to='emprendedor.entrepreneur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrepreneurship',
            name='description',
            field=models.CharField(blank=True, db_column='descripcion', max_length=100, null=True),
        ),
    ]
