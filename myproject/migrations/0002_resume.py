# Generated by Django 4.2.3 on 2023-07-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=60)),
                ('resume', models.FileField(blank=True, null=True, upload_to='projects/resume')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]