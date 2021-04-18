# Generated by Django 3.0.4 on 2021-04-18 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz', '0019_auto_20210418_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=25)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sphere', models.CharField(blank=True, max_length=50)),
                ('question_text', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
