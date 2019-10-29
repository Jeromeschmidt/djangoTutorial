# Generated by Django 2.2.6 on 2019-10-25 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='pub_date',
            field=models.DateTimeField(default=123, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.AddField(
            model_name='choice',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizza'),
        ),
    ]