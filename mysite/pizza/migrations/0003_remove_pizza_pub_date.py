# Generated by Django 2.2.6 on 2019-10-29 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20191025_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='pub_date',
        ),
    ]
