# Generated by Django 3.2.9 on 2022-03-03 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_delete_collect'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
