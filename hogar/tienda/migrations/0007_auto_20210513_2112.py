# Generated by Django 3.1.5 on 2021-05-13 21:12

from django.db import migrations, models
import django.db.models.deletion
import tienda.model_ext.motherboard


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_manufacturer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='front_panel_USB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.frontpanelusb', verbose_name='Front Panel USB'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='category/18.jpg', upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='ethernet',
            name='slug',
            field=models.SlugField(blank=True, default=tienda.model_ext.motherboard.get_RandomString, max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='frame_sync',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.framesync', verbose_name='Frame Suync'),
        ),
        migrations.AlterField(
            model_name='wireless',
            name='slug',
            field=models.SlugField(blank=True, default=tienda.model_ext.motherboard.get_RandomString, max_length=7, unique=True),
        ),
    ]
