# Generated by Django 5.1a1 on 2024-07-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0002_csvfile_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_table',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_table',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
