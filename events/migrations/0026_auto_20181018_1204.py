# Generated by Django 2.1.1 on 2018-10-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20181018_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='Active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='Cat_Level',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='Cat_Name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='category',
            name='Create_date',
            field=models.DateTimeField(default=None, verbose_name='Create Date'),
        ),
        migrations.AddField(
            model_name='category',
            name='Parent_ID',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='create_by',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_by',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_date',
            field=models.DateTimeField(default=None, verbose_name='Update Date'),
        ),
    ]