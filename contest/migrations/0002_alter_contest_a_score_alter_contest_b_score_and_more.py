# Generated by Django 4.1.3 on 2022-12-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='a_score',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='contest',
            name='b_score',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='contest',
            name='c_score',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='contest',
            name='d_score',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
