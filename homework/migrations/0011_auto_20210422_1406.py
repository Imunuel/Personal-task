# Generated by Django 3.0.4 on 2021-04-22 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0010_homework_homeworkresult_personalhomework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkresult',
            name='HM',
        ),
        migrations.RemoveField(
            model_name='personalhomework',
            name='homework_task',
        ),
        migrations.RemoveField(
            model_name='personalhomework',
            name='user',
        ),
        migrations.DeleteModel(
            name='Homework',
        ),
        migrations.DeleteModel(
            name='HomeworkResult',
        ),
        migrations.DeleteModel(
            name='PersonalHomework',
        ),
    ]
