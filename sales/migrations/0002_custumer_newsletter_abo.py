# Generated by Django 5.1.7 on 2025-04-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custumer',
            name='newsletter_abo',
            field=models.BooleanField(default=True),
        ),
    ]
