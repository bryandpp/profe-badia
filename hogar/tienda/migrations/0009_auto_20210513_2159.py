# Generated by Django 3.1.5 on 2021-05-13 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_producto_amount_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherboard',
            name='memoryType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.typememory', verbose_name='Tipo de RAM'),
        ),
    ]
