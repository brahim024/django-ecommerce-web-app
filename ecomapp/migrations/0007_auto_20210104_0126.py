# Generated by Django 3.1.2 on 2021-01-04 00:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_auto_20210103_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
