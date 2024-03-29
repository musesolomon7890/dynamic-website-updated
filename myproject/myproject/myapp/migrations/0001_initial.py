# Generated by Django 5.0.1 on 2024-02-16 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagori_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('product_dis', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('price', models.FloatField(null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('catagories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.catagori')),
            ],
        ),
    ]
