# Generated by Django 4.2.3 on 2023-07-19 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='file',
        ),
    ]