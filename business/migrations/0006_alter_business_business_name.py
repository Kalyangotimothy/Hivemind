# Generated by Django 5.0.3 on 2024-04-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_alter_business_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]