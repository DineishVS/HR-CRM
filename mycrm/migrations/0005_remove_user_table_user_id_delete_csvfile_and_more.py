# Generated by Django 5.1a1 on 2024-07-01 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0004_remove_user_table_email_remove_user_table_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_table',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='CsvFile',
        ),
        migrations.DeleteModel(
            name='user_table',
        ),
    ]
