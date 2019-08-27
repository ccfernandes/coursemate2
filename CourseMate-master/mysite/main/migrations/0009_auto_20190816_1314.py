# Generated by Django 2.2.3 on 2019-08-16 20:14

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190812_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseNumber',
        ),
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='location',
        ),
        migrations.AddField(
            model_name='course',
            name='pop_quizzes',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='professor_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='review_content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 13, 14, 53, 332334), verbose_name='data published'),
        ),
        migrations.AddField(
            model_name='course',
            name='review_title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='numProjects',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 13, 14, 53, 330351), verbose_name='data published'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
