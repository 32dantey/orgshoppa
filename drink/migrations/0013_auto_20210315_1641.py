# Generated by Django 3.1.7 on 2021-03-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0012_auto_20210315_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(blank=True, default='False', help_text='*Fill this field when the delivery has been made*', null=True),
        ),
    ]
