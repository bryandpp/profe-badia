# Generated by Django 3.1.5 on 2021-02-17 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('economia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deudas',
            old_name='fk_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='operaciones',
            old_name='fk_salario',
            new_name='salario',
        ),
        migrations.RenameField(
            model_name='operaciones',
            old_name='fk_tipo_op',
            new_name='tipo_op',
        ),
        migrations.RenameField(
            model_name='operaciones',
            old_name='fk_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='salario',
            old_name='fk_user',
            new_name='user',
        ),
    ]