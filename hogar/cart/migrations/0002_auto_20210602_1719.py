# Generated by Django 3.1.5 on 2021-06-02 17:19

import cart.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_auto_20210601_0247'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.CharField(default=cart.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, default=cart.models.get_RandomString, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=cart.models.generate_uuid, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, default=cart.models.get_RandomString, max_length=10, unique=True)),
                ('date', models.DateField()),
                ('products', models.ManyToManyField(to='tienda.Producto')),
            ],
        ),
        migrations.DeleteModel(
            name='ListaCompra',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='cart.Compras', to='tienda.Producto'),
        ),
        migrations.AddField(
            model_name='cart',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]