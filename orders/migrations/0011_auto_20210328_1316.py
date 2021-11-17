# Generated by Django 3.1.7 on 2021-03-28 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210328_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items_ordered',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_ordered', to='orders.orders'),
        ),
    ]