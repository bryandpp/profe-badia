# Generated by Django 3.1.4 on 2020-12-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0004_auto_20201217_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportes',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='reportes',
            name='file',
            field=models.FileField(null=True, upload_to='media/pdf_repo'),
        ),
    ]