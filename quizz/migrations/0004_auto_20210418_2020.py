# Generated by Django 3.0.4 on 2021-04-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0003_choice_sphere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]