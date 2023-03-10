# Generated by Django 4.1.3 on 2022-12-04 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('registered_user', models.IntegerField(default=0)),
                ('a_score', models.IntegerField()),
                ('b_score', models.IntegerField()),
                ('c_score', models.IntegerField()),
                ('d_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredContestant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_score', models.IntegerField()),
                ('b_score', models.IntegerField()),
                ('c_score', models.IntegerField()),
                ('d_score', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
