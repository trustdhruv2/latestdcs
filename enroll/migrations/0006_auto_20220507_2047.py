# Generated by Django 2.2.6 on 2022-05-07 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_auto_20220506_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainenrollment',
            name='enrolledon',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 20, 47, 22, 944495)),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='enrolledon',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 20, 47, 22, 944495)),
        ),
    ]
