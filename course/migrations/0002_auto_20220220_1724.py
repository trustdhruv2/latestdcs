# Generated by Django 2.2.6 on 2022-02-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='source',
            field=models.TextField(),
        ),
    ]