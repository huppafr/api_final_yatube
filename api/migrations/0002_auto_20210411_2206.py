# Generated by Django 3.2 on 2021-04-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(help_text='Напишите название для группы', max_length=200, unique=True, verbose_name='Название группы'),
        ),
    ]
