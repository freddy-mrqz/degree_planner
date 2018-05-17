# Generated by Django 2.0.4 on 2018-05-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20180509_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='credit_hours',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='course',
            name='cs_concentration',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='is_concentration',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='prereqs',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
