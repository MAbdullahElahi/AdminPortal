# Generated by Django 4.1.13 on 2024-06-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_sales_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Socials',
            field=models.JSONField(blank=True, null=True),
        ),
    ]