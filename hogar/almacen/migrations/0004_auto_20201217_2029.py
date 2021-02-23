# Generated by Django 3.1.4 on 2020-12-17 20:29

import almacen.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_auto_20201208_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.CharField(default=almacen.models.generate_uuid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='almacen',
            name='marca',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='almacen.marca'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='tipo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='almacen.productotipo'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='ubicacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='almacen.posicion'),
        ),
    ]