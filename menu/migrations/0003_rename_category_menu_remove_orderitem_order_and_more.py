# Generated by Django 5.1 on 2024-09-07 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_order_orderitem_order_menu_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Menu',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='menu_item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
