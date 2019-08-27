# Generated by Django 2.2.3 on 2019-08-16 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190816_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 13, 27, 53, 671332), verbose_name='data published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 13, 27, 53, 670099), verbose_name='data published'),
        ),
    ]
