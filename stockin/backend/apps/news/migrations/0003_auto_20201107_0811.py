# Generated by Django 3.1.2 on 2020-11-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201107_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(null=True),
        ),
    ]