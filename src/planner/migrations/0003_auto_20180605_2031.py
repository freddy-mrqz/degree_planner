# Generated by Django 2.0.4 on 2018-06-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20180605_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='saved_path',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='student',
            name='start_term',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring')], default='Fall', max_length=10),
        ),
    ]
