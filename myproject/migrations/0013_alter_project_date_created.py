# Generated by Django 4.2.3 on 2023-07-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0012_project_time_created_alter_project_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]