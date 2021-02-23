# Generated by Django 3.1.4 on 2021-01-08 19:30

from django.db import migrations, models
import listas.models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0006_auto_20210108_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(default=listas.models.generate_uuid_valid, editable=False, max_length=40, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='lista',
            name='nb',
            field=models.CharField(default='Lista NCXY4', max_length=30),
        ),
        migrations.AlterField(
            model_name='lista',
            name='slugUrl',
            field=models.SlugField(default='6X6gZK3BZhF6ZnP0NjGm', editable=False, max_length=20, unique=True),
        ),
    ]