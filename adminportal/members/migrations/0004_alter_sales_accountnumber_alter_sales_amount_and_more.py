# Generated by Django 4.1.13 on 2024-06-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_sales_amount_alter_sales_assignment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='AccountNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Assignment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='ContactNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='DateComplete',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Holder',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Socials',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]