# Generated by Django 3.1.7 on 2021-03-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0014_auto_20210315_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, help_text='*Do not fill this field*', max_length=150, null=True),
        ),
    ]
