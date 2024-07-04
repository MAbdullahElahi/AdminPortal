# Generated by Django 4.1.13 on 2024-06-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=200)),
                ('ContactNumber', models.BigIntegerField()),
                ('Location', models.CharField(default='', max_length=200)),
                ('Assignment', models.CharField(default='', max_length=200)),
                ('Amount', models.FloatField()),
                ('Date', models.DateField(default='')),
                ('DateComplete', models.DateField(default='')),
                ('AccountNumber', models.CharField(default='0000000', max_length=200)),
                ('Socials', models.JSONField()),
                ('Status', models.BooleanField()),
            ],
        ),
    ]