# Generated by Django 5.1.4 on 2024-12-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test product. Currently on a developmental phase so this can be changed during production phase'),
            preserve_default=False,
        ),
    ]
