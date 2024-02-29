# Generated by Django 5.0.1 on 2024-02-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]