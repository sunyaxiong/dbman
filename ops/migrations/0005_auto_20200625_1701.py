# Generated by Django 2.1.5 on 2020-06-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0004_auto_20200610_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbconf',
            name='port',
        ),
        migrations.AlterField(
            model_name='dbconf',
            name='ip',
            field=models.CharField(max_length=128, verbose_name='IP'),
        ),
    ]
