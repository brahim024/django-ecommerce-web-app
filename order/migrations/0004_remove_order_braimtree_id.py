# Generated by Django 3.0.6 on 2020-10-10 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_braimtree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='braimtree_id',
        ),
    ]
