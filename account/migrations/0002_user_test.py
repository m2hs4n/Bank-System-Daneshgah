# Generated by Django 4.2.13 on 2024-06-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
