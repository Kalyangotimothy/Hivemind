# Generated by Django 5.0.3 on 2024-04-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_alter_business_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='contacts',
        ),
    ]