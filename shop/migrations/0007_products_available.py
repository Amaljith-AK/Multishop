# Generated by Django 3.2.11 on 2022-03-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_itemcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
