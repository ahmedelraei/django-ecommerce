# Generated by Django 3.0.5 on 2020-08-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_delete_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDcreated',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at:'),
        ),
    ]
