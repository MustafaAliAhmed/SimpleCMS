# Generated by Django 4.2.4 on 2023-08-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.URLField(auto_created=True),
        ),
    ]
