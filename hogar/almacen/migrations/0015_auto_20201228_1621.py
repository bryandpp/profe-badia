# Generated by Django 3.1.4 on 2020-12-28 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0014_reportes_slug_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.marca'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.productotipo'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.posicion'),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='slug_url',
            field=models.SlugField(blank=True, default='bL3zjSWDlDZgVybgLG08zjzBlLdXxnMw9HT7HNtv', max_length=40, unique=True),
        ),
    ]