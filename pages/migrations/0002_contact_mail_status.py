# Generated by Django 3.0.1 on 2020-07-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mail_status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
