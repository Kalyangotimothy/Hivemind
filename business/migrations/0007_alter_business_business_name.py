# Generated by Django 5.0.3 on 2024-04-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_business_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
