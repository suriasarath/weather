# Generated by Django 2.0 on 2018-04-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analy', '0006_auto_20180412_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre',
            name='humidity',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='pre',
            name='place',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pre',
            name='presure',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='pre',
            name='temp',
            field=models.TextField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='pre',
            name='wind',
            field=models.TextField(default='0', max_length=30),
        ),
    ]
