# Generated by Django 3.0.4 on 2021-04-18 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0009_remove_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='sphere',
        ),
    ]