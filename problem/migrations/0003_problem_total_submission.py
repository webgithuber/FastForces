# Generated by Django 4.1.3 on 2022-12-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_remove_problem_constraints_alter_problem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='total_submission',
            field=models.IntegerField(default=0),
        ),
    ]