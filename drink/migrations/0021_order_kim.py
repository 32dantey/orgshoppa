# Generated by Django 3.1.7 on 2021-03-15 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0020_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='kim',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]