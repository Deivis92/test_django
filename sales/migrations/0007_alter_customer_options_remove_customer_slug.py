# Generated by Django 5.1.7 on 2025-04-06 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_customer_options_customer_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
    ]
