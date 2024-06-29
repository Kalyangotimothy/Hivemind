# Generated by Django 5.0.3 on 2024-04-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_business_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['business_name']},
        ),
        migrations.RemoveField(
            model_name='business',
            name='name',
        ),
        migrations.AddField(
            model_name='business',
            name='business_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]