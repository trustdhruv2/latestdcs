# Generated by Django 2.2.6 on 2022-05-06 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_auto_20220505_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainenrollment',
            name='enrolledon',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 12, 6, 535574)),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='enrolledon',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 12, 6, 535188)),
        ),
    ]