# Generated by Django 3.0.4 on 2021-04-20 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_personalresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalresult',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='personalresult',
            name='task',
        ),
        migrations.RemoveField(
            model_name='personalresult',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='testtask',
            name='question',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='PersonalResult',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='TestTask',
        ),
    ]
