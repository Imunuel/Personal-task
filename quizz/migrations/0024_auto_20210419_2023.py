# Generated by Django 3.0.4 on 2021-04-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0023_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(to='quizz.Choice'),
        ),
    ]