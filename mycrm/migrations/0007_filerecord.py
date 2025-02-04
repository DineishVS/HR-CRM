# Generated by Django 5.1a1 on 2024-07-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrm', '0006_csvfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
