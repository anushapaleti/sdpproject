# Generated by Django 5.0 on 2024-01-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]